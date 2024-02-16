# -*- coding: utf-8 -*-

from odoo import models, fields, api


class paciente(models.Model):
    _name = 'hospital.paciente'
    _description = 'hospital.paciente'
    _rec_name="nombre_completo"

    nombre = fields.Char()
    apellido = fields.Char()
    sintomas = fields.Text("Sintomas del paciente")

    #Añadido de los diagnosticos
    diagnosticos = fields.One2many('hospital.diagnostico','paciente')

    #Campo computado de nombre y apellido
    nombre_completo = fields.Char(compute='_compute_nombre_completo')
    #Funcion para concatenar nombre y apellido
    @api.depends('nombre', 'apellido')
    def _compute_nombre_completo(self):
        for record in self:
            record.nombre_completo = f"{record.nombre} {record.apellido}"