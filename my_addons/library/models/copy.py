# -*- coding: utf-8 -*-

from odoo import fields, models

BOOK_STATE = (
    ('available', 'Available'),
    ('rented', 'Rented'),
    ('lost', 'Lost'),
)


class Copy(models.Model):
    _name = 'library.copy'
    _order = 'id desc'
    _description = 'Library Copy'

    _inherits = {
        'product.product': 'book_id',
    }

    book_id = fields.Many2one('product.product', string='Book', required=True, ondelete="cascade", domain="[('is_book','=',True)]")
    reference = fields.Char(string='Reference', required=True)
    rental_ids = fields.One2many('library.rental', 'copy_id', 'Rental')
    book_state = fields.Selection(selection=BOOK_STATE, string='Book State', default='available')
    active = fields.Boolean("Active", default=True)
