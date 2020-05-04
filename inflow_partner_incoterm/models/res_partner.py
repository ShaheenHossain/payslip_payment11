# -*- coding: utf-8 -*-

from openerp import models, fields, api


class ResPartnerIncoterm(models.Model):
    _inherit = 'res.partner'

    sale_incoterm_id = fields.Many2one(string='Default Sales Incoterm', comodel_name='stock.incoterms', help='The default incoterm for new sales orders for this customer.')
    purchase_incoterm_id = fields.Many2one(string='Default Purchase Incoterm', comodel_name='stock.incoterms',help='The default incoterm for new purchae orders for this supplier.')