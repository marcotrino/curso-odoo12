# -*- coding: utf-8 -*-
{
<<<<<<< HEAD
    'name': "extra-addons/curso-odoo12/library",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
=======
    'name': "Library Management",

    'summary': """
        Library Management
        """,

    'author': "OEC",
    'website': "https://www.odooerpcloud.com",

    'category': 'Tools',
>>>>>>> dev
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
<<<<<<< HEAD
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
=======
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    'installable': True,
}

>>>>>>> dev
