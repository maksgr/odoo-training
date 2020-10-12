# -*- coding: utf-8 -*-

from odoo import fields, models

PARTNER_TYPE = (
    ('customer', 'Customer'),
    ('author', 'Author')
)


class Partner(models.Model):
    _name = 'library.partner'
    _order = 'id desc'
    _description = 'Library Partner'

    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    partner_type = fields.Selection(PARTNER_TYPE, string='Partner Type')
    rental_ids = fields.One2many('library.rental', 'customer_id', string='Rental')
