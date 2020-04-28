# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp


class sh_account_invoice(models.Model):
    _inherit = 'account.invoice'
    
    def _prepare_invoice_line_from_po_line(self, line):
        res = super(sh_account_invoice, self)._prepare_invoice_line_from_po_line(line)
        res.update({
            'sh_sec_qty':line.sh_sec_qty,
            'sh_sec_uom':line.sh_sec_uom.id,
            })
        return res


class sh_customer_invoice_line(models.Model):
    _inherit = "account.invoice.line"
    
    sh_sec_qty = fields.Float("Secondary Qty", digits=dp.get_precision('Product Unit of Measure'))
    sh_sec_uom = fields.Many2one("product.uom", 'Secondary UOM', readonly="onchange_secondary_uom")
    sh_is_secondary_unit = fields.Boolean("Related Sec Uni", related="product_id.sh_is_secondary_unit")
    category_id = fields.Many2one("product.uom.categ", "Category", related="uom_id.category_id")
    
    @api.onchange('quantity', 'uom_id')
    def onchange_product_uom_qty_sh(self):
        if self and self.sh_is_secondary_unit == True and self.sh_sec_uom:
            self.sh_sec_qty = self.uom_id._compute_quantity(self.quantity, self.sh_sec_uom)

    @api.onchange('sh_sec_qty', 'sh_sec_uom')
    def onchange_sh_sec_qty_sh(self):
        if self and self.sh_is_secondary_unit == True and self.uom_id:
            self.quantity = self.sh_sec_uom._compute_quantity(self.sh_sec_qty, self.uom_id)

    @api.multi
    @api.onchange('product_id', 'uom_id')
    def onchange_secondary_uom(self):
        if self:
            for rec in self:
                if rec.product_id.sh_is_secondary_unit == True and rec.product_id.uom_id:
                    rec.sh_sec_uom = rec.product_id.sh_secondary_uom.id
                elif rec.product_id.sh_is_secondary_unit == False:
                    rec.sh_sec_uom = False
                    rec.sh_sec_qty = 0.0
