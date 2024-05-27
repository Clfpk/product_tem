# -*- coding: utf-8 -*-
{
    'name': 'Product Enhance',
    'author': 'Cloud Inf',
    'version': '17.0',
    'license': 'LGPL-3',
    'sequence': 1,
    'depends': ['base','product','purchase'],
    'data': ['security/ir.model.access.csv',
             'views/brand_views.xml',
             'views/model_views.xml',
             'views/price_group_views.xml',
             'views/product_template.xml',
             'views/purchase_order_line.xml'],
    'auto_install': False,
    'application': True,
    'installable': True,
}
