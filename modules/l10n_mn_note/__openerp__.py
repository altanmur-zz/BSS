{
    'name' : 'Note',
    'version' : '1.1',
    'author' : 'Altanmur',
    'category' : 'Note',
    'description' : """al ledgers are done through the defined Financial Journals (entry move line or grouping is maintained through a journal) 
for a particular financial year and for preparation of vouchers there is a module named account_voucher.
    """,
    'website': 'https://www.odoo.com/page/billing',
    'depends' : ['note'],
    'update_xml': [
        'inherit_note_view.xml'
    ],
    'installable': True,
    'auto_install': False,
}