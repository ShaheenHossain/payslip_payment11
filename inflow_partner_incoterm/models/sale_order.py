# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Sale(models.Model):
    _inherit = 'sale.order'

    @api.onchange('partner_id')
    def on_change_sale_incoterms(self):
        for rec in self:
            if rec.partner_id:
                rec.incoterm = rec.partner_id.sale_incoterm_id
