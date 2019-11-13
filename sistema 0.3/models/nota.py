# -*- coding: utf-8 -*-

from odoo import models, fields


class Nota(models.Model):
    _name = 'sistema.nota'
    _description = 'Lista de notas de alumnos'

    id_nota = fields.Integer(string='numero de nota', required=True)
    id_alumno = fields.Many2one('sistema.alumno', 'rut_alumno')
    id_asignatura = fields.Many2one('sistema.asignatura', 'id_asignatura')
    