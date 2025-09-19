{
    'name': 'Student Management',
    'version': '1.0',
    'summary': 'Manage students and courses in Odoo',
    'description': """
        A custom module to manage student information, courses,
        and student enrollments in various courses.
    """ ,
    'author': 'Jahid',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/course_views.xml',
        'views/course_report_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
