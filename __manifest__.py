{
    'name': 'Purchase Order Enhancement',
    'version': '1.0',
    'license': 'LGPL-3',
    'description': 'This module contains enhanced features for Purchase module',
    'depends': ['base', 'purchase'],
    'author': 'John Bui',
    'application': True,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',

        'views/purchase_order_views.xml',
        'wizard/purchase_order_archive_views.xml',
        'report/purchase_order_templates.xml',
        # 'report/purchase_report_views.xml'
        'data/ir_cron_data.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'purchase_order_enhancement/static/src/js/us_phone.js',
        ]
    },
}