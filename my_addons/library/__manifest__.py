# -*- coding: utf-8 -*-

{
    'name': "Library Management",

    'summary':
    """
        Library management
    """,

    'description':
    """
        Manage a Library: customers, books, etc.... 
    """,

    'author': "Odoo",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Library',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends':
        ['base', 'product', 'purchase'],

    # always loaded
    'data':
    [
        "security/ir.model.access.csv",
        "data/library_data.xml",
        "data/ir_cron_data.xml",
        "views/library_view.xml",
        "views/partner_view.xml",
        "views/rentals_view.xml",
        "views/product_view.xml",
        "views/copy_view.xml",
        "views/price_view.xml",
        "views/payment_view.xml",
    ],
    # only loaded in demonstration mode
    'demo': [],
    'license': 'AGPL-3',
}
