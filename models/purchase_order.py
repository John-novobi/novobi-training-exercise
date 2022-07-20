from odoo import fields, models
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    _description = 'Purchase Order Enhancement'

    active = fields.Boolean(string='Active', default=True)

    def action_archive_purchase_order(self):
        for record in self:
            if record.state in ('done', 'cancel'):
                record.active = False
            else:
                raise UserError('Can only archive Locked or Canceled Purchase Order')