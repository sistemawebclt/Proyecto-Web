# -*- coding: utf-8 -*-

from odoo import models, fields


class Asignatura(models.Model):
    _name = 'sistema.asignatura'
    _description = 'Lista de asignaturas'

    id_asignatura = fields.Integer(string='numero asignatura', required=True)
    id_profesor = fields.Many2one('sistema.profesor', 'rut_profesor')
    nombre_asignatura = fields.Char('nombre asignatura', required=True)
    id_nota = fields.One2many('sistema.nota', 'id_nota')