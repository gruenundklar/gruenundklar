# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    cid = fields.Char('Kundennummer', copy=False, index=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            for v in vals:
                if str(v) == 'cid':
                    val = self.env['ir.sequence'].next_by_code('res.partner.cid')
                    vals['cid'] = val
        return super(ResPartner, self).create(vals_list)

