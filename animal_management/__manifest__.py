{
    'name': "Animal Management",
    'summary': "Modul ini digunakan untuk management animal",
    'description': """
        modul ini akan dikembangkan lagi
    """,
    'author': "Dito",
    'website': "http://www.dito.odoo.com",
    'category': 'Uncategorized',
    'version': '14.0.1',
    'depends': ['base'],
    'data': [
        'views/am_appointment_views.xml',
        'views/am_stage_views.xml',
        'views/am_service_views.xml',
        'views/am_menuitem_views.xml',
        'views/am_pemeriksaan_views.xml',
    ],
    
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
