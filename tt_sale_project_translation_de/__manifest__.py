# -*- coding: utf-8 -*-
# Copyright TrendTec UG (haftungsbeschränkt)
# Autor: Oliver Kölsch

{
    'name': 'Artikelerweiterung Feld Zolltarifnummer',
    'version': '1.0.14',
    'category': 'TrendTec/Extensions',
    'sequence': 16,
    'summary': 'Erweiterungen des Artikels um das Feld Zolltarifnummer',
    'description': "Erweiterungen des Artikels um das Feld Zolltarifnummer",
    'schortdesc': "Erweiterungen des Artikels um das Feld Zolltarifnummer",
    'website': 'https://www.trendtec.de/shop/odoo-benutzererweiterung-feld-kundennummer-1005',
    'license': 'AGPL-3',
    'maintainer': 'TrendTec (development@trendtec.de)',
    'author': 'TrendTec (development@trendtec.de)',
    'support': 'support@trendtec.de',
    'depends': [
        'stock',
        'tt_product_template_freitext_1'
    ],
    'website': 'https://www.trendtec.de/shop/odoo-benutzererweiterung-feld-kundennummer-1005',
    'data': [
        'views/product_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False
}