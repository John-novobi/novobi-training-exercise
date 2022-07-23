from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    archive_lifespan = fields.Integer(string='Archive lifespan (minutes)', config_parameter='purchase_order_archive_lifespan', default=30)
    