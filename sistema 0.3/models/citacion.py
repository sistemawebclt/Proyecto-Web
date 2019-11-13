# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import date

class Citacion(models.Model):
    _name = 'sistema.citacion'
    _description = 'Lista de citaciones'

    id_citacion = fields.Integer(string='numero citacion', required=True)
    id_profesor = fields.Many2one('sistema.profesor', 'rut_profesor')
    rut_apoderado = fields.Many2one('sistema.apoderado','rut_apoderado')
    fecha_citacion = fields.Datetime(string='fecha de citacion', required=True)
    asunto = fields.Char('asunto citacion', required=True)