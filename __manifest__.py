# -*- coding: utf-8 -*-
{
    'name': "DietFacts",

    'summary': """
            DietFacts: modulo de teste para a vaga de estágio na Bradoo
        """,

    'description': """
            Módulo para controlar fatos de dieta a partir do banco de dados aberto da DietFacts
    """,

    'author': "VictorTineo",
    'website': "github.com/victortineo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'DietFacts',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/dietfacts__menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
