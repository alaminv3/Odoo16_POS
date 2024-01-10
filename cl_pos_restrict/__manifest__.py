# -*- coding: utf-8 -*-
{
    'name': "Custom Pos Development",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Al-amin",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Pos',
    'version': '16.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'cl_pos_restrict/static/src/js/inherit_numpad_widget.js',
            'cl_pos_restrict/static/src/xml/inherit_numpad_widget.xml',
        ]
    }
}
