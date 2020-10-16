# -*- coding: utf-8 -*-

from odoo import fields, models

TYPE = (
    ('time', 'Time'),
    ('one', 'One')
)


class Price(models.Model):
    _name = 'library.price'
    _order = 'id desc'
    _description = 'Library Price'

    name = fields.Char(string="Name")
    duration = fields.Float(string="Duration")
    price = fields.Float(string="Price")
    type = fields.Selection(selection=TYPE, string='Type', default='time')
