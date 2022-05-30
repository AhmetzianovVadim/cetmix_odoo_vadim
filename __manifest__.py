# -*- coding: utf-8 -*-
{
    'name': "cx_test_base_two_vadim",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale', 'project'],

    # always loaded
    'data': ["data/task_number_sequence.xml",
             "views/sale_order_line.xml",
             "report/sale_order_report.xml",
             "views/sale_show_all_order_line.xml",
             "views/fields_required.xml",
             "views/task_number.xml"
             ],

    # only loaded in demonstration mode
    'demo': [],
}
