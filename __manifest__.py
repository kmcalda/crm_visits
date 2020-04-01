# -*- coding: utf-8 -*-
{
    'name': "Visits",
    'summary': """
        Visits module for CRM""",
    'website': 'https://github.com/kmcalda/custom_module',
    'author': "Kevin Marvin Calda",
    'category': 'Extra tool',
    'version': '0.1',
    'license': 'AGPL-3',
    'sequence': 10,
    'depends': [
        'crm',
    ],
    'data': [
        'views/visits_menu.xml',
        'views/visits_menu.xml',
    ],
    'application': True,
    'installation': True,
    'auto_install': False,
}