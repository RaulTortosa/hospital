from odoo import models, fields, api


class diagnostico(models.Model):
    _name = 'hospital.diagnostico'
    _description = 'hospital.diagnostico'

    #Campo medico con relacion a la tabla medico
    medico = fields.Many2one(comodel_name="hospital.medico")
    #Campo paciente con relacion a la tabla paciente
    paciente = fields.Many2one(comodel_name="hospital.paciente")
    descripcion = fields.Text("Diagnostico")