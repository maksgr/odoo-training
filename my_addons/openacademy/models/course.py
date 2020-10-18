# -*- coding: utf-8 -*-

from odoo import fields, models, api

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
    responsible_id = fields.Many2one('res.partner', string="Responsible")
    session_ids = fields.One2many('session', 'course_id', string="Session")
    level = fields.Selection(LEVEL, string='Level')
    attendee_count = fields.Integer(string='Attendee Count', compute='_compute_attendee')

    @api.depends('session_ids.attendees_count', 'session_ids.attendee_ids')
    def _compute_attendee(self) -> None:
        for record in self:
            record.attendee_count = record.session_ids.attendees_count + len(record.session_ids.attendee_ids.ids)
