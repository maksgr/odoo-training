# -*- coding: utf-8 -*-

from odoo import fields, models


class Payment(models.Model):
    _name = 'library.payment'
    _order = 'id desc'
    _description = 'Library Payment'

    date = fields.Date(string='Date', default=fields.Date.context_today, required=True)
    amount = fields.Float(string='Amount')
    customer_id = fields.Many2one('res.partner', 'Customer', domain="[('partner_type','=','customer')]")
