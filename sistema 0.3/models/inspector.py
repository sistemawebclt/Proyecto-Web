# -*- coding: utf-8 -*-

from odoo import models, fields

class Inspector(models.Model):
    _name = 'sistema.inspector'
    _rec_name = 'nombres_inspector'
    _description = 'Lista con la información de los inspectores del colegio'

    
    rut_inspector = fields.Char('Rut inspector', required=True)
    nombres_inspector = fields.Char('Nombre Inspector', required=True)
    fecha_ingreso_inspector = fields.Date(string='fecha de ingreso al establecimiento', required=True)
    correo_inspector = fields.Char('correo inspector',required=True)
    