# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BusinessPartnerClusterCluster(models.Model):
    _name = 'business.partner.cluster'
    _description = 'Business Partner Cluster'

    name = fields.Char(string='Regional Cluster', help='Enter Industrial Cluster Region', required=True)
    cluster_code = fields.Char(string='Cluster Code', help='Enter Industrial Cluster Region Code', required=True)
    state_id = fields.Many2one('res.country.state', string='State Name', required=True)




