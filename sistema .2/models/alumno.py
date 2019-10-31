# -*- coding: utf-8 -*-

from odoo import models, fields

class Alumno(models.Model):
    _name = 'sistema.alumno'
    _rec_name = 'nombres_alumno'
    _description = 'Lista con la información de los alumnos del colegio'

    
    rut_alumno = fields.Char('Rut Alumno', required=True)
    nombres_alumno = fields.Char('Nombres Alumno', required=True)
    apellidos_alumno = fields.Char('Apellidos Alumno', required=True)
    fecha_nacimiento_alumno = fields.Date(string='Fecha de Nacimiento', required=True)
    comuna_alumno = fields.Char('Comuna Alumno', required=True)
    domicilio_alumno = fields.Char('domicilio Alumno', required=True)
    procedencia_alumno = fields.Char('Escuela de Origen',)
    fecha_ingreso_alumno = fields.Date(string='fecha de ingreso al establecimiento', required=True)
    cursos_repetidos = fields.Integer(string='cantidad de veces que repitió curso',)
    nombre_madre = fields.Char('nombre madre', required=True)
    nombre_padre = fields.Char('nombre padre', required=True)
    vive_con = fields.Char(string='Vive con:',)
    info_salud = fields.Char('ingresar datos de salud estudiante',)
    info_varias = fields.Char('ingresar información de consideración')
    caso_emergencia = fields.Char('en caso de emergencia llamar a', required=True)
    fono_emergencia = fields.Char('telefono emergencia', required=True)
    cod_curso = fields.Many2one('sistema.curso', 'Curso')
    