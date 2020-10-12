# -*- coding: utf-8 -*-

from odoo import fields, models


class Copy(models.Model):
    _name = 'library.copy'
    _order = 'id desc'
    _description = 'Library Copy'

    _inherits = {
        'library.book': 'book_id',
    }

    book_id = fields.Many2one('library.book', string='Book', required=True, ondelete="cascade")
    reference = fields.Char(string='Reference')
    rental_ids = fields.One2many('library.rental', 'copy_id', 'Rental')
