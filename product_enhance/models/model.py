from odoo import models, fields

class Model(models.Model):
    _name = 'product.model'
    _description = 'Model'

    name = fields.Char('Name', required=True)
    brand_id = fields.Many2one('product.brand', 'Brand', required=True)
    category_id = fields.Many2one('product.category', string="Category")
