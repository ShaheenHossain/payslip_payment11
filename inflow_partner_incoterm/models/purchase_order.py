# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Purchase(models.Model):
    _inherit = 'purchase.order'

    @api.onchange('partner_id')
    def on_change_purchase_incoterms(self):
        for rec in self:
            if rec.partner_id:
                rec.incoterm_id = rec.partner_id.purchase_incoterm_id
