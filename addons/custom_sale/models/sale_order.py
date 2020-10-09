# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        self.env.cr.execute('''
            SELECT sp.id
            FROM sale_order so
            JOIN sale_order_line sol ON sol.order_id = so.id
            JOIN stock_picking sp ON sp.sale_id = so.id
            WHERE sol.express_shipping != False AND so.id IN %s
            GROUP BY sp.id
            HAVING count(sol.id) >= 2
        ''', (tuple(self.ids),))
        stock_picking_id = self.env.cr.fetchone() or False
        if stock_picking_id:
            self.env['stock.picking'].browse(stock_picking_id[0]).copy().id
        return res
