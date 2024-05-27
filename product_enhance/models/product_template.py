
from odoo import models, fields


class Brand(models.Model):
    _inherit = 'product.template'

    # brand_name = fields.Char(string='Brand Name', required=True)
    model_name = fields.Char(string='Model Name', required=True)
    # category_id = fields.Many2one('product.template', string="Category")
    brand_id = fields.Many2one('product.brand', string='Brand', required=True)