# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp


class sh_inventory_adjustment(models.Model):
    _inherit = 'stock.inventory.line'
    
    sh_sec_qty = fields.Float("Secondary Qty", digits=dp.get_precision('Product Unit of Measure'))
    sh_sec_uom = fields.Many2one("product.uom", 'Secondary UOM', related="product_id.sh_secondary_uom", readonly=False)
    sh_is_secondary_unit = fields.Boolean("Related Sec Uni", related="product_id.sh_is_secondary_unit")
    category_id = fields.Many2one("product.uom.categ", "Category", related="product_uom_id.category_id")

    @api.onchange('product_qty', 'product_uom_id')
    def onchange_product_uom_qty_sh(self):
        if self and self.sh_is_secondary_unit == True and self.sh_sec_uom:
            self.sh_sec_qty = self.product_uom_id._compute_quantity(self.product_qty, self.sh_sec_uom)

    @api.onchange('sh_sec_qty', 'sh_sec_uom')
    def onchange_sh_sec_qty_sh(self):
        if self and self.sh_is_secondary_unit == True and self.product_uom_id:
            self.product_qty = self.sh_sec_uom._compute_quantity(self.sh_sec_qty, self.product_uom_id)
