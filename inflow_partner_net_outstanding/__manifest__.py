# -*- coding: utf-8 -*-

{
    'name': 'Business Parter Outstanding Amount',
    'summary': """Net Parnter Outstanding Amount in Sale/Purchase Form""",
    'version': '11.0.1.0.1',
    'description': """
    Amount Payable & Receivable In Partner Form
    """,
    'author': 'Vaibhav Misra',
    'company': 'Inflow Industrial Solutions',
    'website': 'http://www.inflow.co.in',
    'category': 'Accounting',
    'depends': ['base', 'account', 'sale', 'purchase'],
    'license': 'LGPL-3',
    'data': [
        'views/sale_order_view.xml',
        'views/purchase_order_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
