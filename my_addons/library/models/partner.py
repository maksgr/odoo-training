# -*- coding: utf-8 -*-

from odoo import fields, models, api

PARTNER_TYPE = [
    ('customer', 'Customer'),
    ('author', 'Author'),
    ('publisher', 'Publisher')
]


class Partner(models.Model):
    _inherit = 'res.partner'

    partner_type = fields.Selection(selection=PARTNER_TYPE, string='Partner Type')
    rental_ids = fields.One2many('library.rental', 'customer_id', string='Rentals')
    payment_ids = fields.One2many('library.payment', 'customer_id', 'Payments')
    amount_owd = fields.Float(string='Amount owd', compute='_amount_owd')

    @api.depends('payment_ids.amount')
    def _amount_owd(self):
        for partner in self:
            partner.amount_owd = sum(operation.amount for operation in partner.payment_ids)
