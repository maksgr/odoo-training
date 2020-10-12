# -*- coding: utf-8 -*-

from odoo import fields, models


class Publisher(models.Model):
    _name = 'library.publisher'
    _order = 'id desc'
    _description = 'Library Publisher'

    name = fields.Char(string='Name')
