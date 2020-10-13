# -*- coding: utf-8 -*-

from odoo import fields, models


class Partner(models.Model):
    _name = 'partner'
    _order = 'id desc'
    _description = 'Partner'

    name = fields.Char(string='Name', required=True)
    instructor = fields.Boolean('Instructor')
