# -*- coding: utf-8 -*-

from odoo import models, fields

class detalleAtraso(models.Model):
    _name = 'sistema.detalle_atraso'
    _description = 'Lista con la información de los atrasos del colegio'

    razon_atraso = fields.Char('razón del atraso')
    adulto_responsable = fields.Char('quien trae al alumno')

    atraso_id = fields.Many2one('sistema.atraso')