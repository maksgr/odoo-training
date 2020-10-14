# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import ValidationError, _logger

STATE = (
    ('draft', 'Draft'),
    ('confirmed', 'Confirmed'),
    ('done', 'Done')
)


class Session(models.Model):
    _name = 'session'
    _inherit = ['mail.thread']
    _order = 'id desc'
    _description = 'Session'

    name = fields.Char(string='Name', required=True)
    state = fields.Selection(STATE, string='Status', default='draft')
    start_date = fields.Date(string='Start Date', default=fields.Date.context_today)
    end_date = fields.Date(string='End Date', default=fields.Date.context_today)
    duration = fields.Float('Duration', default=1)  # need to do default one day
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('course', string="Course", required=True, ondelete='cascade')
    attendee_ids = fields.Many2many('res.partner', 'res_partner_rel', 'instructor_id', string='Partner')
    active = fields.Boolean('Active', default=True)

    seats = fields.Integer(string='Seats')
    taken_seats = fields.Float(compute='_compute_taken_seats', string='Taken Seats')

    @api.depends('attendee_ids', 'seats')
    def _compute_taken_seats(self) -> None:
        for record in self:
            if record.attendee_ids.ids and record.seats:
                record.taken_seats = 100 * len(record.attendee_ids.ids) / record.seats
            else:
                record.taken_seats = 0.0

    @api.constrains('attendee_ids', 'seats')
    def _check_taken_seats(self):
        for record in self:
            if record.taken_seats > 100:
                raise ValidationError("The percentage of occupied seats should be from 0 to 100.")

    def button_draft(self) -> None:
        self.write({'state': 'draft'})

    def button_confirm(self) -> None:
        self.write({'state': 'confirmed'})

    def button_done(self) -> None:
        self.write({'state': 'draft'})

    def state_confirmed(self) -> None:
        if self.taken_seats > 50 and self.state == 'draft':
            self.button_confirm()

    @api.model
    def create(self, values) -> super:
        res = super(Session, self).create(values)
        body_message = 'Session Name: %s, Course Name: %s, State: %s' % (res.name, res.course_id.name, res.state)
        subject_message = 'Create - "%s"!' % res.name
        res.send_message(subject_message, body_message)
        res.state_confirmed()
        return res

    def write(self, values: dict) -> super:
        res = super(Session, self).write(values)
        body_message = 'Session Name: %s, Course Name: %s, State: %s' % (self.name, self.course_id.name, self.state)
        subject_message = 'Write - "%s"!' % self.name
        self.send_message(subject_message, body_message)
        self.state_confirmed()
        return res

    def create_mail_channel(self) -> object:
        return self.env['mail.channel'].with_context({
            'mail_create_nolog': True,
            'mail_create_nosubscribe': True,
            'mail_channel_noautofollow': True,
        }).create({
            'name': self.name,
            'email_send': False,
            'channel_type': 'chat',
            'public': 'public',
            'channel_partner_ids': [(4, self.instructor_id.id)]
        })

    def send_message(self, subject_message: str, body_message: str):
        try:
            channel_obj = self.env['mail.channel'].search([('name', 'like', self.name)])
            if not channel_obj:
                channel_obj = self.create_mail_channel()
            channel_obj.message_post(
                subject=subject_message,
                body=body_message,
                message_type='comment',
                subtype='mail.mt_comment',
            )
        except Exception as e:
            _logger.critical(e)
            raise ValidationError("Sorry something went wrong.")
