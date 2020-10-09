# -*- coding: utf-8 -*-

from odoo import models, fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    express_shipping = fields.Boolean("Express Shipping", default=False)
