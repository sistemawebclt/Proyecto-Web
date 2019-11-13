# -*- coding: utf-8 -*-
{
    'name': "Sistema Club de Leones",

    'summary': """
        Sistema de información""",

    'description': """
        Sistema para el manejo de atrasos, comportamiento y citaciones del colegio
    """,

    'author': "IIE Módulo Web II, SSM, CT, CV",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/menu.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/profesor.xml',
        'views/alumno.xml',
        'views/apoderado.xml',
        'views/atraso.xml',
        'views/detalle_atraso.xml',
        'views/curso.xml',
        'views/inspector.xml',
        'views/asignatura.xml',
        'views/citacion.xml',
        'views/nota.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}