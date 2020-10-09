# -*- coding: utf-8 -*-

{
    'name': "Castom Sale",
    'version': '13.0.1.0.0',
    'summary': "Keep the records of employee blood details",
    'description': "Keep the records of employee blood details",
    'category': 'Human Resources',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'depends': ['base', 'hr'],
    'data': [
        'view/sale_order_view.xml',
        'security/ir.model.access.csv',
    ],
    'license': "AGPL-3",
    'installable': True,
    'application': True,
}
