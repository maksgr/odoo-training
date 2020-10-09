# -*- coding: utf-8 -*-

from odoo import fields, models


class Partner(models.Model):
    _name = 'res.partner'
    _order = 'id desc'
    _description = 'Partner'

    name = fields.Char(string='Name', required=True)
    instructor = fields.Boolean('Instructor', readonly=True)
    responsible_id = fields.Many2one('res.partner', string="Responsible")
    session_ids = fields.One2many(string="Session", comodel_name='account.tax.report.line', inverse_name='parent_id')
