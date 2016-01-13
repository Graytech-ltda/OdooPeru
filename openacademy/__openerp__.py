{
'name':"OpenAcademy",
    'version' : '3.0',
    'author' : 'Juan Sepulveda & William Genoy',
    'category' : 'Training',
    'description' : """
        MANAGEMENT COURSE, SESSION AND ATTENDEE
    """,
    'website': 'https://www.odoo.com',
    'depends' : ['base','mail'],
    'data': [
             'openacademy.xml', 
             'partner_view.xml',
             'report/openacademy_report_view.xml',
    ],
    'qweb' : [
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
}