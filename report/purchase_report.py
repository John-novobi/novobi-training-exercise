from odoo import fields, models

class PurchaseReport(models.Model):
    _inherit = 'purchase.report'

    payment_term_id = fields.Many2one(comodel_name='account.payment.term', string='Payment Term')

    def _select(self):
        return super(PurchaseReport, self)._select() + ', po.payment_term_id as payment_term_id'

    def _group_by(self):
        return super(PurchaseReport, self)._group_by() + ', po.payment_term_id'
