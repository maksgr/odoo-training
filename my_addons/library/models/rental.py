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
    customer_address = fields.Text('Customer Address', related='customer_id.address')
    customer_email = fields.Char('Customer Email', related='customer_id.email')
    book_author_ids = fields.Many2many(related='book_id.author_ids')
    book_edition_date = fields.Date(string='Edition Date', related='book_id.edition_date')
    book_publisher_id = fields.Many2one(related='book_id.publisher_id')
