# -*- coding: utf-8 -*-

from odoo import fields, models


LEVEL = (
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('hard', 'Hard')
)


class Course(models.Model):
    _name = 'course'
    _order = 'id desc'
    _description = 'Course'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    responsible_id = fields.Many2one('partner', string="Responsible")
    session_ids = fields.One2many('partner', 'course_id', string="Session")
    level = fields.Selection(LEVEL, string='Level')
