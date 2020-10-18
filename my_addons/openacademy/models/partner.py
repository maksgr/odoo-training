# -*- coding: utf-8 -*-

from odoo import fields, models, api


class Partner(models.Model):
    _inherit = 'res.partner'

    course_id = fields.Many2one('course', string='Course')
    instructor = fields.Boolean('Instructor')
    session_ids = fields.Many2many('session', 'session_rel', 'instructor_id', string='Sessions', readonly=True)
    course_attendee_count = fields.Integer(related="course_id.attendee_count")

    def show_attendee(self):
        self.ensure_one()
        action = self.env.ref('openacademy.session_action_tree').read()[0]
        return action
