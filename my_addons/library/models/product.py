# -*- coding: utf-8 -*-

from odoo import fields, models, api


class Product(models.Model):
    _inherit = 'product.product'

    isbn = fields.Char(string='Isbn', required=True)
    author_ids = fields.Many2many('res.partner', string='Partner', domain="[('partner_type','=','author')]")
    publisher_id = fields.Many2one('res.partner', string='Publisher', domain="[('partner_type','=','publisher')]")
    edition_date = fields.Date(string='Edition Date')
    rental_ids = fields.One2many('library.rental', 'book_id', 'Rental')
    copy_ids = fields.One2many('library.copy', 'book_id', 'Copy')
    is_book = fields.Boolean("Book")

    _sql_constraints = [
        ('unique_isbn', 'unique (isbn)', 'Field "Isbn" already exists with this value!')
    ]

