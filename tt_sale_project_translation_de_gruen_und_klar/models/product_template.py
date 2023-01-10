# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _, SUPERUSER_ID
import logging

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def _selection_service_policy(self):
        _logger.log("started")
        service_policies = [
            # (service_policy, string)
            ('ordered_prepaid', 'Vorkasse/Festpreis'),
            ('delivered_manual', 'basierend auf geleiferten Produkten'),
        ]
        if self.user_has_groups('project.group_project_milestone'):
            service_policies.insert(1, ('delivered_milestones', 'basierend auf Stundenzetteln'))
        return service_policies
