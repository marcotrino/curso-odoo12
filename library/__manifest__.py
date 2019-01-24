# -*- coding: utf-8 -*-
{
    'name': "Library Management",

    'summary': """
        Library Management
        """,


    'author': "OEC_VALERO",
    'website': "http://www.soefitecsas.com",


    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'installable': True,
}
