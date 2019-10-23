# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import date

class Atraso(models.Model):
    _name = 'sistema.atraso'
    _description = 'Lista con la información de los atrasos del colegio'

    fecha_atraso = fields.Datetime('Date current action', required=False, readonly=False, select=True, default=lambda self: fields.datetime.now())
    
    detalle_atraso_ids = fields.Many2one('sistema.detalle_atraso', 'atraso_id')