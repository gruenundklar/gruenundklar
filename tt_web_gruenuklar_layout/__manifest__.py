# -*- coding: utf-8 -*-
# Copyright TrendTec UG (haftungsbeschränkt)
# Autor: Oliver Kölsch

{
    'name': 'Individuelles Template Grün & Klar',
    'version': '1.0.16',
    'category': 'TrendTec/Extensions',
    'sequence': 16,
    'summary': 'Individuelles Template Grün & Klar',
    'description': "Individuelles Template Grün & Klar",
    'website': 'https://www.trendtec.de/shop/odoo-erweiterung-bank',
    'author': 'TrendTec (development@trendtec.de)',
    'license': 'AGPL-3',
    'maintainer': 'TrendTec(development@trendtec.de)',
    'support': 'support@trendtec.de',
    'depends': [
        'base',
        'web',
        'account',
        'sale'
    ],
    'website': 'https://www.trendtec.de/shop/odoo-erweiterung-bank',
    'data': [
        'views/report_templates.xml',
        'views/account_move_views.xml',
        'data/report_layout.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False
}