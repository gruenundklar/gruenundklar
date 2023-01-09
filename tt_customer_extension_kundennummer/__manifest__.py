# -*- coding: utf-8 -*-
# Copyright TrendTec UG (haftungsbeschränkt)
# Autor: Oliver Kölsch

{
    'name': 'Benutzererweiterung Feld Kundennummer',
    'version': '1.0.12',
    'category': 'TrendTec/Extensions',
    'sequence': 16,
    'summary': 'Erweiterungen des Kontaktes um das Feld Kundennummer',
    'description': "Erweiterungen des Kontaktes um das Feld Kundennummer",
    'schortdesc': "Erweiterungen des Kontaktes um das Feld Kundennummer",
    'website': 'https://www.trendtec.de/shop/odoo-benutzererweiterung-feld-kundennummer-1005',
    'license': 'AGPL-3',
    'maintainer': 'TrendTec (development@trendtec.de)',
    'author': 'TrendTec (development@trendtec.de)',
    'support': 'support@trendtec.de',
    'depends': [

    ],
    'website': 'https://www.trendtec.de/shop/odoo-benutzererweiterung-feld-kundennummer-1005',
    'data': [
        'views/res_partner.xml',
        'data/kundennummer_data.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False
}