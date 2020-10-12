# -*- coding: utf-8 -*-

from odoo import fields, models


class Rental(models.Model):
    _name = 'library.rental'
    _order = 'id desc'
    _description = 'Library Rental'

    name = fields.Char(string='Name')
    customer_id = fields.Many2one('library.partner', 'Customer')
    book_id = fields.Many2one('library.book', 'Book')
    rental_date = fields.Date(string='Rental Date')
    return_date = fields.Date(string='Return Date')

