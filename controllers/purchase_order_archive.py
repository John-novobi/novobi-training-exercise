from odoo import http
from odoo.http import request, route
from odoo.exceptions import MissingError, UserError, ValidationError

class PurchaseOrderArchive(http.Controller):
    @route(['/purchase_order/archive'], methods=['POST'], type='json', auth='none')
    def archive_purchase_order(self, **params):
        def _parse_request(params):
            method = params.get('method')
            order_ids = params.get('orders')
            if not method or not order_ids:
                raise UserError('Invalid parameters')
            if method != 'archive':
                raise ValidationError('Invalid method')
            return {
                'method': method,
                'order_ids': order_ids
            }

        def _get_order_ids(order_ids):
            found_order_ids = request.env['purchase.order'].sudo().browse(order_ids)
            if len(found_order_ids.exists()) != len(order_ids):
                raise MissingError('Could not found')
            else:
                return found_order_ids

        def _success_response(order_ids):
            return {
                'archived_orders': order_ids,
                'code': 200,
                'message': 'Successful'
            }

        def _fail_response(code, message):
            return {
                'archived_orders': False,
                'code': code,
                'message': message
            }
        
        response = {}
        try:
            request_data = _parse_request(params)
            _get_order_ids(request_data['order_ids']).action_archive_purchase_order(api_call=True)
            response = _success_response(request_data['order_ids'])
        except ValidationError as e:
            response = _fail_response(code=422, message=e)
        except MissingError as e:
            response = _fail_response(code=404, message=e)
        except UserError as e:
            response = _fail_response(code=400, message=e)
        except:
            response = _fail_response(code=500, message='Internal server error')
        return response
