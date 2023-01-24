# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _, SUPERUSER_ID
import logging

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sales.order'
    bearbeiter = fields.Selection([('Roland Grabenauer', 'Roland Grabenauer'),
                                      ('Sascha Hotz', 'Sascha Hotz'),
                                      ], string='Sachbearbeiter', default='Roland Grabenauer')
