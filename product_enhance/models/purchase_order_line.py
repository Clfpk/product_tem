from odoo import models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    category_id = fields.Many2one('product.category', string='Category')
    brand_id = fields.Many2one('product.brand', string='Brand')
    model_id = fields.Many2one('product.model', string='Model')
    price_group = fields.Many2one('product.price.group', string='Price Group')

    @api.onchange('category_id')
    def onchange_category_id(self):
        if self.category_id:
            return {'domain': {'brand_id': [('category_id', '=', self.category_id.id)]}}

    @api.onchange('brand_id')
    def onchange_brand_id(self):
        if self.brand_id:
            return {'domain': {'model_id': [('brand_id', '=', self.brand_id.id)]}}

    @api.onchange('model_id', 'price_group_id')
    def onchange_model_price_group_id(self):
        if self.model_id and self.price_group:
            return {'domain': {'product_id': [
                ('categ_id', '=', self.category_id.id),
                ('brand_id', '=', self.brand_id.id),
                ('model_id', '=', self.model_id.id),
                ('price_group_id', '=', self.price_group_id.id),
            ]}}
