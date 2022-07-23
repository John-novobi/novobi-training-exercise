from dateutil.relativedelta import relativedelta

from odoo import api, fields, models
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    _description = 'Purchase Order Enhancement'

    active = fields.Boolean(string='Active', default=True)
    hotline = fields.Char(string='Hotline')

    def action_archive_purchase_order(self, api_call=False):
        if api_call or self.env.user.user_has_groups('purchase.group_purchase_manager'):
            self._archive_purchase_order()
        else:
            raise UserError('Only Purchase Manager can archive Purchase Order')

    def _archive_purchase_order(self):
        if self.filtered(lambda record: record.state not in ('done', 'cancel')).exists():
            raise UserError('Can only archive Locked or Canceled Purchase Order')
        else:
            self.write({'active': False})
                

    @api.model
    def cron_archive_old_purchase_order(self):
        lifespan = int(self.env['ir.config_parameter'].sudo().get_param('purchase_order_archive_lifespan', 30))
        date_threshold = fields.Datetime.now() - relativedelta(minutes=lifespan)
        self.search([('state','in',['done','cancel']),('write_date','<',date_threshold)])._archive_purchase_order()
