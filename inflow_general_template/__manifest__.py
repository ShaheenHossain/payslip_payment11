# -*- coding: utf-8 -*-

{
    'name': 'Inflow All In One Report Templates',
    'author': 'Vaibhav Misra',
    'version': '11.1.1',
    'category': 'Reporting',
    'depends': [
        'account',
        'sale_management',
        'delivery',
        'stock',
        'purchase',
        'inflow_gst_india_calculation',
        'sh_secondary_unit',
        'l10n_in_sale',
        'l10n_in_purchase',
        'l10n_in_stock',
    ],
    'website': 'www.inflow.co.in',
    'description': '''Get Diverse Templates For PO/RFQ/SO/Delivery Note/Picking List!
Professional templates
Professional Report Templates
Sales Order Report Template
Quotation Report Template
Purchase order Report Template
Purchase Requestion Template
Credit Memo Report Template
Picking List report Template
SO report template
Po Report Template
Report
report template
advance report template
advanced report template
custom report template
custom report
report designer
multiple report templates
Odoo multiple report templates
report app
advance report app
odoo report template
odoo report app
odoo custom report

Development - In process
Pl Note it works only with the Advanced Theme only for now.

''',
    'summary': 'Get Diverse Templates For PO/RFQ/SO/Delivery Note/Picking List One Go!',
    'data': [
        'security/base_security.xml',
        'security/ir.model.access.csv',
        # 'data/template_data.xml',
        'views/custom_header_footer.xml',
        # 'views/report_extra_content_view.xml',

        'views/templates.xml',  # Added file of global templates
        'views/sale_templates.xml',
        'views/invoice_templates.xml',
        'views/quotation_templates.xml',
        'views/purchase_templates.xml',
        'views/picking_templates.xml',

        'views/web_widget_color_view.xml',
        'views/template_report.xml',
        'views/res_company_view.xml',
        'views/res_partner_view.xml',
        'views/sale_view.xml',
        'views/stock_view.xml',
        'views/purchase_view.xml',
        'views/invoice_view.xml',
        'views/preview_template.xml',

        #'views/creative_sale.xml',
        #'views/elegant_sale.xml',
        #'views/professional_sale.xml',
        #'views/exclusive_sale.xml',
        #'views/advanced_sale.xml',
        #'views/custom_sale.xml',
        #'views/incredible_sale.xml',
        #'views/innovative_sale.xml',

        #'views/advanced_delivery.xml',
        #'views/creative_delivery.xml',
        #'views/elegant_delivery.xml',
        #'views/professional_delivery.xml',
        #'views/exclusive_delivery.xml',
        #'views/custom_delivery.xml',
        #'views/incredible_delivery.xml',
        #'views/innovative_delivery.xml',

        #'views/advanced_picking.xml',
        #'views/creative_picking.xml',
        #'views/elegant_picking.xml',
        #'views/professional_picking.xml',
        #'views/exclusive_picking.xml',
        #'views/custom_picking.xml',
        #'views/incredible_picking.xml',
        #'views/innovative_picking.xml',

        #'views/creative_purchase.xml',
        #'views/elegant_purchase.xml',
        #'views/professional_purchase.xml',
        #'views/exclusive_purchase.xml',
        #'views/advanced_purchase.xml',
        #'views/custom_purchase.xml',
        #'views/incredible_purchase.xml',
        #'views/innovative_purchase.xml',

        #'views/advanced_quotation.xml',
        #'views/creative_quotation.xml',
        #'views/elegant_quotation.xml',
        #'views/professional_quotation.xml',
        #'views/exclusive_quotation.xml',
        #'views/custom_quotation.xml',
        #'views/incredible_quotation.xml',
        #'views/innovative_quotation.xml',

        'views/creative_template.xml',
        'views/elegant_template.xml',
        'views/professional_template.xml',
        'views/exclusive_template.xml',
        'views/advanced_template.xml',
        'views/custom_template.xml',
        'views/incredible_template.xml',
        'views/innovative_template.xml',

    ],
    'qweb': [
        'static/src/xml/widget_color.xml',
    ],
    'images': ['static/description/splash-screen.png'],
    'external_dependencies': {'python': ['num2words']},
    'installable': True,
    'auto_install': False,
    'web_preload': True,
}
