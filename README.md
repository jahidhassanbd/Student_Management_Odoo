# Student Management Module

Student Management is a custom Odoo application designed to manage students and courses.
With this module, you can:

Store and manage student information (name, email, roll number, department).

Define courses (course code, name, credits).

Enroll a student in multiple courses (many-to-many relationship).

View which students are enrolled in which courses, and how many students are enrolled per course.

Features

✅ Student records with unique roll numbers

✅ Course records with unique course codes

✅ Many-to-many relationship between Students ↔ Courses

✅ Tree, Form, and Search views for both models

✅ Easy navigation through Students and Courses menus

✅ Report: View how many students are enrolled in each course

Steps to Install & Test

Copy the student_management folder into your Odoo addons directory.

Add the student_management folder path to the addons_path in your odoo.conf.

Restart the Odoo server:

python odoo-bin -c odoo.conf


Log in to Odoo and go to the Apps menu.

Search for Student Management and install it.

Start using the module via Student Management → Students / Courses menus.

Challenges & Solutions

❌ Issue: Python version mismatch (Odoo 19 did not work with Python 3.11).
✔ Solution: Switching to Python 3.10 solved the problem.

❌ Issue: Some dependencies (e.g., libsass) were not installing.
✔ Solution: Installing Microsoft C++ Build Tools resolved the issue.


✍ Author: Jahid
📌 Version: 1.0.0
🛠 Odoo Compatibility: Odoo 19

