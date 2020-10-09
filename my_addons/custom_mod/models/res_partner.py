# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    primary_address = fields.Boolean("Primary Address", default=False)

    def check_express_shipping(self, company_id):
        """
        This function checks the presence of an active checkbox
        on Contacts & Addresses belonging to one company
        :param company_id:
        :return: partner_id
        """
        if not company_id:
            return False
        self._cr.execute("""
            SELECT id
            FROM res_partner
            WHERE type = 'delivery'
            AND parent_id = %s
            """, (company_id,))
        return self._cr.fetchone() or False

    def deactivate_express_shipping(self, id, company_id):
        """
        This function deactivate field express shipping if they belong to the same company

        :param id:
        :param company_id:
        :return: True
        """
        self._cr.execute("""
            UPDATE res_partner
            SET primary_address = False
            WHERE type = 'delivery'
            AND parent_id = %s
            AND id <> %s
            """, (company_id, id))
        return True

    @api.model
    def create(self, values):
        primary_address = values.get('primary_address')
        company_id = values.get('parent_id', False)
        check_express_shipping = self.check_express_shipping(company_id)
        if company_id and primary_address:
            self.deactivate_express_shipping(None, company_id)
        elif primary_address is False and not check_express_shipping:
            values.update({'primary_address': True})
        return super(ResPartner, self).create(values)

    def write(self, values):
        if self.type == 'delivery' or values.get('type') == 'delivery' and 'primary_address' in values:
            company_id = self.parent_id.id or values.get('parent_id')
            if not self.check_express_shipping(company_id):
                values.update({'primary_address': True})
            elif values.get('primary_address') is True:
                self.deactivate_express_shipping(self.id, company_id)
                values.update({'primary_address': True})
        return super(ResPartner, self).write(values)
