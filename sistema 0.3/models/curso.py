# -*- coding: utf-8 -*-

from odoo import models, fields


class Curso(models.Model):
    _name = 'sistema.curso'
    _description = 'Lista de cursos del Colegio'

    cod_curso = fields.Char('Grado Curso', required=True)
    numero_sala = fields.Char('número de sala', required=True)
    cantidad_alumnos = fields.Char('cantidad alumnos', required=True)
    id_profesor = fields.Many2one('sistema.profesor', 'asignar profesor')
    id_alumno = fields.One2many('sistema.alumno', 'rut_alumno')