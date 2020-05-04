# -*- coding: utf-8 -*-

from odoo import fields, models


class ResPartner(models.Model):

    _inherit = 'res.partner'

    cluster_id = fields.Many2one('business.partner.cluster', string='Regional Cluster')
    partner_company_type = fields.Selection([('private', 'Private Enterprise'),('public', 'Public Sector Enterprise'),('proprietorship', 'Proprietorship Enterprise'),('government', 'Government Enterprise')], string='Company Type')
    partner_vendor_type = fields.Selection([('primary', 'Primary'),('secondary', 'Secondary'),('tertiary', 'Tertiary')], string='Vendor Type')
    partner_customer_type = fields.Selection([('small', 'Small'),('medium', 'Medium'),('large', 'Large')], string='Customer Type')
    partner_pan_number = fields.Char(string='PAN Number', size=10, help='Business Partner PAN Number')
    partner_cin_number = fields.Char(string='CIN Number', size=21, help='Partner CIN Number')