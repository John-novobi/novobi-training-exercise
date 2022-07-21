from odoo import http
from odoo.http import request, route
from odoo.exceptions import UserError

class PurchaseOrderArchive(http.Controller):
    @route(['/purchase_order/archive'], methods=['POST'], type='json', auth='none')
    def archive_purchase_order(self, **params):
        method = params['method']
        if method != 'archive':
            raise UserError('Invalid method !')
        order_ids = params['orders']
        try:
            request.env['purchase.order'].sudo().browse(order_ids).action_archive_purchase_order()
            return {
                'archived_orders': order_ids,
                'code': 200,
                'message': 'Successful'
            }
        except:
            return {
                'archived_orders': False,
                'code': 404,
                'message': 'Could not found'
            }