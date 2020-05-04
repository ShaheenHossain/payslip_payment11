# -*- coding: utf-8 -*-

from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    credit = fields.Monetary(string='Total Receivables', related='partner_id.credit')
    debit = fields.Monetary(string='Total Payables', related='partner_id.debit')
    total_receivables = fields.Monetary(string='Net Receivables', compute='_get_total')

    @api.one
    def _get_total(self):
        self.total_receivables = self.credit - self.debit
        return True