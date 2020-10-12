# -*- coding: utf-8 -*-

from odoo import fields, models


class Book(models.Model):
    _name = 'library.book'
    _order = 'id desc'
    _description = 'Library Book'

    name = fields.Char(string='Name')
    author_ids = fields.Many2many('library.partner', 'author_rel', 'book_id', string='Partner')
    edition_date = fields.Date(string='Edition Date')
    isbn = fields.Char(string='Isbn')
    publisher_id = fields.Many2one('library.publisher', string='Publisher')
    rental_ids = fields.One2many('library.rental', 'book_id', 'Rental')
    copy_ids = fields.One2many('library.copy', 'book_id', 'Copy')
