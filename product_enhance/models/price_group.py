from odoo import models, fields, api

class PriceGroup(models.Model):
    _name = 'price.group'
    _description = 'Price Group'

    name = fields.Char(string='Price Group Name', required=True)
    price_from = fields.Float(string='From', required=True)
    price_to = fields.Float(string='To', required=True)
    display_name = fields.Char(string='Display Name', compute='_compute_display_name', store=True)

    @api.depends('name', 'price_from', 'price_to')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} ({record.price_from} - {record.price_to})"
