# -*- coding: utf-8 -*-

from odoo import models, fields

class Apoderado(models.Model):
    _name = 'sistema.apoderado'
    _rec_name = 'nombres_apoderado'
    _description = 'Lista con la información de los apoderadoes del colegio'
    
    rut_apoderado = fields.Char('Rut apoderado', required=True)
    nombres_apoderado = fields.Char('Nombres apoderado', required=True)
    apellidos_apoderado = fields.Char('Apellidos apoderado', required=True)
    telefono_apoderado = fields.Char('Telefono apoderado', required=True)
    email_apoderado = fields.Char('Correo Electronico Apoderado', required=True)
    comuna_apoderado = fields.Char('Comuna apoderado', required=True)
    domicilio_apoderado = fields.Char('domicilio apoderado', required=True)
