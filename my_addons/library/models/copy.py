# -*- coding: utf-8 -*-

from odoo import fields, models, api

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
    readers_count = fields.Integer(string='Readers Count', compute='_compute_readers_count')

    @api.depends('rental_ids.customer_id')
    def _compute_readers_count(self):
        for record in self:
            record.readers_count = len(record.rental_ids.ids) if record.rental_ids.ids else None

    def open_readers(self):
        self.ensure_one()
        action = self.env.ref('library.res_partner_action_tree').read()[0]
        action['domain'] = [('rental_ids', 'in', self.rental_ids.ids)]
        return action
