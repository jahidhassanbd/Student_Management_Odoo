from odoo import fields, models

class Course(models.Model):
    _name = 'student.management.course'
    _description = 'Course'
    _order = 'code asc'

    name = fields.Char(string='Course Name', required=True)
    code = fields.Char(string='Course Code', required=True, copy=False)
    credit = fields.Integer(string='Credits')
    student_ids = fields.Many2many(
        'student.management.student',
        'student_course_rel',
        'course_id',
        'student_id',
        string='Enrolled Students'
    )

    _sql_constraints = [
        ('code_unique', 'unique(code)', 'Course Code must be unique!'),
    ]
