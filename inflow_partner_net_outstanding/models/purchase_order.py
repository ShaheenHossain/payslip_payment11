# -*- coding: utf-8 -*-

from odoo import api, fields, models

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    credit = fields.Monetary(string='Total Receivables', related='partner_id.credit')
    debit = fields.Monetary(string='Total Payables', related='partner_id.debit')
    total_payables = fields.Monetary(string='Net Payables', compute='_get_total')

    @api.one
    def _get_total(self):
        self.total_payables = self.debit - self.credit
        return True