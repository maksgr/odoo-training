# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        sol_ids = self.order_line.ids
        Picking = self.env['stock.picking']
        res = super(SaleOrder, self).action_confirm()
        active_express_shipping = self.env['sale.order.line'].browse(self.order_line.ids).\
            filtered(lambda l: l.express_shipping is True)
        if len(sol_ids) >= 2 and active_express_shipping:
            stock_move_ids = self.env['stock.move'].search([
                ('sale_line_id', 'in', active_express_shipping.ids)
            ])
            pk_id = Picking.create(stock_move_ids._get_new_picking_values())
            stock_move_ids.write({'picking_id': pk_id.id})
            stock_move_ids.mapped('move_line_ids').write({'picking_id': pk_id.id})
        return res
