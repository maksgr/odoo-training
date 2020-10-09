# -*- coding: utf-8 -*-
{
    'name': "custom_mod",

    'summary': """Custom MOD""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Maksym Hrybun",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'sale'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order_view.xml',
        'views/pes_partner_view.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
