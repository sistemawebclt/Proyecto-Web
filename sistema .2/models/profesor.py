# -*- coding: utf-8 -*-

from odoo import models, fields

class Profesor(models.Model):
    _name = 'sistema.profesor'
    _rec_name = 'nombres_profesor'
    _description = 'Lista con la información de los profesores del colegio'

    
    rut_profesor = fields.Char('Rut Profesor', required=True)
    nombres_profesor = fields.Char('Nombres Profesor', required=True)
    apellidos_profesor = fields.Char('Apellidos Profesor', required=True)
    especialidad_profesor = fields.Char('Especialidad Profesor', required=True)
    fecha_nacimiento_profesor = fields.Date(string='Fecha de Nacimiento', required=True)
    telefono_profesor = fields.Char('Telefono Profesor', required=True)
    comuna_profesor = fields.Char('Comuna Profesor', required=True)
    domicilio_profesor = fields.Char('domicilio Profesor', required=True)
    fecha_ingreso_profesor = fields.Date(string='fecha de ingreso al establecimiento', required=True)
