# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Daily Reports',
    'version' : '1.1',
    'summary': 'Daily Work Reports',
    'sequence': 10,
    'description': """
        Submit and view daily work reports
    """,
    'category': 'reporting',
    'website': 'https://www.odoo.com/page/billing',
    'depends' : ['base'],
    'data': [
            'security\ir.model.access.csv',
            'security\security.xml',
            'views\\report_card_view.xml'
            ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
