from odoo import api, fields, models
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    _description = 'Purchase Order Enhancement'

    active = fields.Boolean(string='Active', default=True)
    lifespan = fields.Integer(string='Lifespan', default=30)
    hotline = fields.Char(string='Hotline')

    def action_archive_purchase_order(self):
        if not self.env.user or self.env.user.user_has_groups('purchase.group_purchase_manager'):
            self._archive_purchase_order()
        else:
            raise UserError('Only Purchase Manager can archive Purchase Order')

    def _archive_purchase_order(self):
        for record in self:
            if record.state in ('done', 'cancel'):
                record.active = False
            else:
                raise UserError('Can only archive Locked or Canceled Purchase Order')

    @api.model
    def cron_archive_old_purchase_order(self):
        self.search([
            '|',('state','=','done'),('state','=','cancel')
        ]).filtered(lambda record: record.lifespan < (fields.Datetime.today() - record.write_date).seconds // 60)._archive_purchase_order()