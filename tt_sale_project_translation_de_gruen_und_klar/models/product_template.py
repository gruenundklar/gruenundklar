# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _, SUPERUSER_ID
import logging

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def _selection_service_policy(self):
        service_policies = super()._selection_service_policy()
        _logger.info(service_policies)
        service_policies_new = []
        for policy in service_policies:
            _logger.info(policy)
            for pol in policy:
                if str(pol) == 'ordered_prepaid':
                    service_policies_new.insert(1, ('ordered_prepaid', 'Vorkasse/Festpreis'))
                if str(pol) == 'delivered_manual':
                    service_policies_new.insert(2, ('delivered_manual', 'basierend auf gelieferten Produkten'))
                if str(pol) == 'delivered_timesheet':
                    service_policies_new.insert(3, ('delivered_timesheet', 'basierend auf Stundenzetteln'))
                if str(pol) == 'delivered_milestones':
                    service_policies_new.insert(4, ('delivered_milestones', 'basierend auf Meilensteinen'))
        return service_policies_new
