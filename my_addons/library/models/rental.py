# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.addons.base.models.ir_mail_server import MailDeliveryException, _logger

STATE = (
    ('draft', 'Draft'),
    ('rented', 'Rented'),
    ('returned', 'Returned'),
    ('lost', 'Lost')
)


class Rental(models.Model):
    _name = 'library.rental'
    _order = 'id desc'
    _description = 'Library Rental'

    name = fields.Char(string='Name')
    copy_id = fields.Many2one('library.copy', string='Copy')
    customer_id = fields.Many2one('res.partner', 'Customer')
    book_id = fields.Many2one(related='copy_id.book_id', readonly=True)
    rental_date = fields.Date(string='Rental Date')
    return_date = fields.Date(string='Return Date')
    planned_return_date = fields.Date(string='Planned Return Date')
    customer_address = fields.Char('Customer Address', related='customer_id.street')
    customer_email = fields.Char('Customer Email', related='customer_id.email')
    book_author_ids = fields.Many2many(related='book_id.author_ids')
    book_edition_date = fields.Date(string='Edition Date', related='book_id.edition_date')
    book_publisher_id = fields.Many2one(related='book_id.publisher_id')
    state = fields.Selection(STATE, 'State')

    def add_fee(self, price_type) -> object:
        price_rent_obj = self.env.ref('library.price_rent')
        if price_type == 'time':
            number_day_rent = self.return_date - self.rental_date
            amount = number_day_rent.days * price_rent_obj.price / price_rent_obj.duration
        else:
            amount = self.env.ref('library.price_loss').price
        return self.env['library.payment'].create({
            'date': self.rental_date,
            'amount': amount,
            'customer_id': self.customer_id.id
        })

    def action_confirm(self) -> None:
        self.write({'state': 'rented'})
        self.copy_id.write({'book_state': 'rented'})
        self.add_fee('time')

    def action_return(self) -> None:
        self.write({'state': 'returned'})
        self.copy_id.write({'book_state': 'available'})

    def action_lost(self) -> None:
        self.write({'state': 'lost'})
        self.copy_id.write({'book_state': 'lost', 'active': False})
        self.add_fee('lost')

    def action_send(self) -> None:
        for customer in self.customer_id:
            subject = 'Debtor: %s' % customer.name
            template_id = self.env.ref('library.debtor_mail_template')
            template_id.with_context(user=customer.user_id).send_mail(
                self.id, force_send=True, raise_exception=True,
                email_values={'email_to': customer.email, 'subject': subject})

    def _cron_check_date(self):
        debtors = self.search([
            ('rental_date', '<', fields.Date.today()),
            ('state', '=', 'rented')
        ])
        for debtor in debtors:
            try:
                debtor.action_send()
            except MailDeliveryException as e:
                _logger.warning('MailDeliveryException while sending digest %d. Digest is now scheduled for next cron update.')
