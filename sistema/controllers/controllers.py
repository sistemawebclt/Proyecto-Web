# -*- coding: utf-8 -*-
from odoo import http

# class Addons/sistema(http.Controller):
#     @http.route('/addons/sistema/addons/sistema/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addons/sistema/addons/sistema/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addons/sistema.listing', {
#             'root': '/addons/sistema/addons/sistema',
#             'objects': http.request.env['addons/sistema.addons/sistema'].search([]),
#         })

#     @http.route('/addons/sistema/addons/sistema/objects/<model("addons/sistema.addons/sistema"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addons/sistema.object', {
#             'object': obj
#         })