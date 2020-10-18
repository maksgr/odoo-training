# -*- coding: utf-8 -*-

from odoo import fields, models, api


class AddBookWizard(models.Model):
    _name = 'add.book.wizard'

    copy_ids = fields.Many2many('library.copy', string='Copy')
    customer_id = fields.Many2one('res.partner', string='Customer')
    rental_id = fields.Many2one('library.rental', string='Rental')
    return_date = fields.Date(string='Return Date')

    @api.model
    def default_get(self, fields) -> object:
        result = super(AddBookWizard, self).default_get(fields)
        book_ids = self._context.get('active_ids')
        if book_ids:
            result['copy_ids'] = [(6, 0, book_ids)]
        return result

    def continue_add_book(self) -> True:
        rental_obj = self.env['library.rental']
        for copy in self.copy_ids:
            rental_id = rental_obj.create({
                'book_id': copy.id,
                'customer_id': self.customer_id.id,
                'return_date': self.return_date
            })
            self.customer_id.update({'rental_ids': [(6, 0, rental_id.id)]})
        self.rental_id.write({'state': 'draft'})
        return True
