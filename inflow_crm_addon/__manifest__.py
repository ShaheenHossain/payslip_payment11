# -*- coding: utf-8 -*-

{
    'name': 'Crm Lead Addon',
    'summary': """Makes salesperson auto visible and expected closing as mandatory""",
    'version': '11.0.1.0.1',
    'description': """
    Makes salesperson auto visible and expected closing as mandatory
    """,
    'author': 'Vaibhav Misra',
    'company': 'Inflow Industrial Solutions',
    'website': 'http://www.inflow.co.in',
    'category': 'Sales',
    'depends': ['base', 'crm', 'sale'],
    'license': 'LGPL-3',
    'data': [
        'views/crm_lead_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
