from odoo import fields, models

class Student(models.Model):
    _name = 'student.management.student'
    _description = 'Student'
    _order = 'roll_no asc'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    roll_no = fields.Char(string='Roll Number', required=True, copy=False)
    department = fields.Char(string='Department')
    course_ids = fields.Many2many(
        'student.management.course',
        'student_course_rel',
        'student_id',
        'course_id',
        string='Courses Enrolled'
    )

    _sql_constraints = [
        ('roll_no_unique', 'unique(roll_no)', 'Roll Number must be unique!'),
    ]

    def action_show_courses(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Enrolled Courses',
            'res_model': 'student.management.course',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', self.course_ids.ids)],
        }
