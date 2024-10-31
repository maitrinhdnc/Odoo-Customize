{
    'name': 'Contact Extend',
    'version': '1.0',
    'depends': ['contacts'],
    'data': [
        'views/res_partner_groups_views.xml',
        'views/res_partner_views.xml',
        'security/contact_groups_security.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'license': 'LGPL-3'
}
