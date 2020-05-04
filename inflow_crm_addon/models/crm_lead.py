# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.onchange('partner_id')
    def on_change_crm_lead_partner_id(self):
        for rec in self:
            if rec.partner_id:
                if rec.partner_id.user_id:
                    rec.user_id = rec.partner_id.user_id
