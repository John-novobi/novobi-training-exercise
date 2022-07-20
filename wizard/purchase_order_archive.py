from odoo import fields, models

class PurchaseOrderArchive(models.TransientModel):
    _name = 'purchase.order.archive'
    _description = 'Purchase Order Archive'

    purchase_order_ids = fields.Many2many(comodel_name='purchase.order', string='Purchase Orders')

    def action_archive_purchase_orders(self):
        for record in self:
            record.purchase_order_ids.action_archive_purchase_order()