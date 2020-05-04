#################################################################################
# Author      : Inflow Industrial Solutions. (<https://inflow.co.in/>)
# Copyright(c): 2015-Present Inflow Industrial Solutions
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://inflow.co.in/>
#################################################################################
# -*- coding: utf-8 -*-

{
    'name': 'Business Partner Additional Information',
    'version': '11.0.1.0',
    'category': 'Generic Modules/Sales Management',
    'description': """
This module adds additional information to Business Partner which are both Customer/Supplier:
1. Industrial Cluster
2. Type of Partner     
3. Vendor Type - Primary, Secondary, Tertiary
4. Pan Number
5. CIN No
6. Customer Size - Small, Medium, Large           
    """,
    'summary': 'This app will add additional fields in the Business Parter Form',
    'depends': ['sale', 'stock', 'account', 'purchase', 'account_voucher', 'sale_approve', 'dev_customer_flow'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_cluster.xml',
        'views/res_partner.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,

    # author and support Details
    'author': 'Vaibhav Misra',
    'website': 'http://www.inflow.co.in',
    'maintainer': 'Vaibhav Misra',
    'support': 'vaibhav.v13@gmail.com',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
