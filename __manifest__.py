# -*- coding: utf-8 -*-
{
    'name': "Hospital",

    'summary': "Pequeño modulo para administrar pacientes y medicos",

    'description': """
Modulo para administrar los pacientes y sus sintomas y los medicos que tienen asignados
    """,

    'application': True,
    'author': "Raul Rodriguez Tortosa",
    'website': "https://github.com/RaulTortosa",
    'category': 'Productivity',
    'version': '0.1',
    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/medico.xml',
        'views/paciente.xml',
        'views/diagnostico.xml'
    ],
}