# -*- coding: utf-8 -*-

from odoo import fields, models


class Partner(models.Model):
    _name = 'partner'
    _order = 'id desc'
    _description = 'Partner'

    name = fields.Char(string='Name', required=True)
    instructor = fields.Boolean('Instructor')
    course_id = fields.Many2one('course', string='Course')
    session_ids = fields.Many2many('session', 'session_rel', 'instructor_id', string='Sessions', readonly=True)
