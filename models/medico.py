# -*- coding: utf-8 -*-

from odoo import models, fields, api


class medico(models.Model):
    _name = 'hospital.medico'
    _description = 'Medico'
    _rec_name="nombre_completo"

    nombre = fields.Char()
    apellido = fields.Char()
    numeroColegiado = fields.Integer("Numero de colegiado")

    #Añadido de los diagnosticos
    diagnosticos = fields.One2many('hospital.diagnostico','medico')

    #Campo computado de nombre y apellido
    nombre_completo = fields.Char(compute='_compute_nombre_completo')
    #Funcion para concatenar nombre y apellido
    @api.depends('nombre', 'apellido')
    def _compute_nombre_completo(self):
        for record in self:
            record.nombre_completo = f"{record.nombre} {record.apellido}"