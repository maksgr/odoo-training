# -*- coding: utf-8 -*-

from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    course_id = fields.Many2one('course', string='Course')
    instructor = fields.Boolean('Instructor')
    session_ids = fields.Many2many('session', 'session_rel', 'instructor_id', string='Sessions', readonly=True)
