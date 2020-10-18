# -*- coding: utf-8 -*-

from odoo import fields, models, api


class AddAttendeesWizard(models.Model):
    _name = 'add.attendees.wizard'

    session_id = fields.Many2one('session', string='Session')
    attendee_ids = fields.Many2many('res.partner', string='Attendees')

    @api.model
    def default_get(self, fields):
        result = super(AddAttendeesWizard, self).default_get(fields)
        partner_ids = self._context.get('active_ids')
        if partner_ids:
            result['attendee_ids'] = [(6, 0, partner_ids)]
        return result

    def subscribe_attendee(self):
        for wiz in self:
            wiz.session_id.update({'attendee_ids': [(6, 0, wiz.attendee_ids.ids)]})
