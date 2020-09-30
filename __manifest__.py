# -*- coding: utf-8 -*-
{
    'name': "Vencimientos Cheques",

    'summary': """ Compara la fecha de pago de los cheques con la fecha de hoy y calcula los
    días restantes. """,

    'description': """
        Ordena vista tree de cheques, de forma descendente
    """,

    'author': "Lucio Bisiach",
    'website': " -  ",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '11.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account_check'],

    # always loaded
    'data': [
        'views/order_tree_view_check.xml',
    ],
    # only loaded in demonstration mode
    'demo': [ ],
}