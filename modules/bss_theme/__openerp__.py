{
    'name': 'BSS Theme',
    'summary': 'Support for Bootswatch themes in master',
    'description': 'This theme module is exclusively for master to keep the support of Bootswatch themes which were previously part of the website module in 8.0.',
    'category': 'Theme',
    'version': '1.0',
    'author': 'Aptena',
    'depends': ['website'],
    'data': [
        # 'views/theme.xml',
        # 'views/test.xml',
        'views/blocks/blocks.xml',
        'views/header_footer/language.xml',
        'views/layout/body.xml',
        'views/position/layout.xml',
    ],
    'images': ['static/description/bootswatch.png'],
    'application': False,
}
