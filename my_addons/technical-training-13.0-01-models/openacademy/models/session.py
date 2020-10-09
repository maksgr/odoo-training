# -*- coding: utf-8 -*-

from odoo import fields, models


STATE = (
    ('draft', 'Draft'),
    ('confirmed', 'Confirmed'),
    ('done', 'Done')
)

class Session(models.Model):
    _name = 'res.session'
    _order = 'id desc'
    _description = 'Session'

    name = fields.Char(string='Name', required=True)
    state = fields.Selection(STATE, string='Status', default='draft')
    start_date = fields.Date(string='Start Date', default=fields.Date.context_today)
    end_date = fields.Date(string='End Date', default=fields.Date.context_today)
    duration = fields.Float('Duration', digits=(0, 1))
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('res.course', string="Course", required=True, ondelete='cascade')
    attendee_ids = fields.Many2many('res.partner', string='Partner')
    active = fields.Boolean('Active', default=True)

