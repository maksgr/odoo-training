# -*- coding: utf-8 -*-
# from odoo import http


# class MySaleOrder(http.Controller):
#     @http.route('/custom_mod/custom_mod/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_mod/custom_mod/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_mod.listing', {
#             'root': '/custom_mod/custom_mod',
#             'objects': http.request.env['custom_mod.custom_mod'].search([]),
#         })

#     @http.route('/custom_mod/custom_mod/objects/<model("custom_mod.custom_mod"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_mod.object', {
#             'object': obj
#         })
