# -*- coding: utf-8 -*-

from odoo import fields, models, api

STATE = (
    ('draft', 'Draft'),
    ('confirmed', 'Confirmed'),
    ('done', 'Done')
)


class Session(models.Model):
    _name = 'session'
    _order = 'id desc'
    _description = 'Session'

    name = fields.Char(string='Name', required=True)
    state = fields.Selection(STATE, string='Status', default='draft')
    start_date = fields.Date(string='Start Date', default=fields.Date.context_today)
    end_date = fields.Date(string='End Date', default=fields.Date.context_today)
    duration = fields.Float('Duration', default=1)  # digits=(0, 1)
    instructor_id = fields.Many2one('partner', string="Instructor")
    course_id = fields.Many2one('course', string="Course", required=True, ondelete='cascade')
    attendee_ids = fields.Many2many('partner', 'partner_rel', 'instructor_id', string='Partner')
    active = fields.Boolean('Active', default=True)

    # Task 3

    seats = fields.Integer(string='Seats')
    taken_seats = fields.Float(compute='_compute_taken_seats', string='Taken Seats')

    @api.depends('attendee_ids', 'seats')
    def _compute_taken_seats(self):
        for record in self:
            record.taken_seats = 100 * record.attendee_ids.ids / record.seats

    def _check_taken_seats(self):
        for record in self:
            if record.taken_seats > 100:
                return True

    _constraints = [(_check_taken_seats, 'Please inter other qty !', ['qty'])]

