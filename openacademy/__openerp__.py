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
             'openacademy_workflow.xml',
             'security/groups.xml',
             'security/ir.model.access.csv',
             'wizard/enroll_view.xml',
             'report/report_session.xml',
             'report/report_session_excel.xml',
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