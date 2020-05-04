# -*- coding: utf-8 -*-

{
    'name': 'Business Parter Default Incoterm',
    'summary': """Default Patner Incoterm in Sale/Purchase Form""",
    'version': '11.0.1.0.1',
    'description': """
    Adds a default Incoterm in the Business Partner for Sale and Purchase
    """,
    'author': 'Vaibhav Misra',
    'company': 'Inflow Industrial Solutions',
    'website': 'http://www.inflow.co.in',
    'category': 'Accounting',
    'depends': ['base', 'stock', 'sale', 'purchase', 'dev_customer_flow'],
    'license': 'LGPL-3',
    'data': [
        'views/res_partner_form.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
