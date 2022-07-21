from odoo import fields, models

class PurchaseReport(models.Model):
    _inherit = 'purchase.report'

    payment_term_id = fields.Char(related='order_id.payment_term_id.name', store=True)