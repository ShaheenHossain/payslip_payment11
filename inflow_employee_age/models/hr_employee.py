# -*- coding: utf-8 -*-

from dateutil.relativedelta import relativedelta
from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    age = fields.Integer(
        string='Age',
        readonly=True,
        compute='_compute_age',
    )

    @api.multi
    @api.depends('birthday')
    def _compute_age(self):
        for record in self:
            age = 0
            if record.birthday:
                age = relativedelta(
                    fields.Date.from_string(fields.Date.today()),
                    fields.Date.from_string(record.birthday)).years
            record.age = age
