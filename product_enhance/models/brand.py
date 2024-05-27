from odoo import models, fields

class Brand(models.Model):
    _name = 'product.brand'
    _description = 'Brand'

    name = fields.Char('Name', required=True)
    category_id = fields.Many2one('product.category', string="Category")