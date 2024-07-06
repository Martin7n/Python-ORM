import os
import django
from datetime import date



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Student

print(Student.objects.all())

# Run and print your queries


def add_students():
    new_st1 = Student(student_id="FC5204", first_name="John", last_name="Doe", birth_date="1995-05-15", email="john.doe@university.com")
    new_st2 = Student(student_id="FE0054", first_name="Jane", last_name="Smith",  email="jane.smith@university.com")
    new_st3 = Student(student_id="FH2014", first_name="Alice", last_name="Johnson", birth_date="1998-02-10", email="alice.johnson@university.com")
    new_st4 = Student(student_id="FH2015", first_name="Bob", last_name="Wilson", birth_date="1996-11-25", email="bob.wilson@university.com")
    new_objs = [new_st1, new_st2, new_st3, new_st4]
    for x in new_objs:
        x.save()
# add_students()


def add_students1():

    new_st1 = Student(student_id="FC6204", first_name="John", last_name="Doe", birth_date="1995-05-15", email="john.d1e@university.com")
    new_st2 = Student(student_id="FE6054", first_name="Jane", last_name="Smith",  email="jane.sm1th@university.com")
    new_st3 = Student(student_id="FH6014", first_name="Alice", last_name="Johnson", birth_date="1998-02-10", email="al1ce.johnson@university.com")
    new_st4 = Student(student_id="FH6015", first_name="Bob", last_name="Wilson", birth_date="1996-11-25", email="bob.w1lson@university.com")
    new_objs = [new_st1, new_st2, new_st3, new_st4]
    Student.objects.bulk_create(new_objs)
# add_students1()

def get_students_info():
    result = []
    students = Student.objects.all()
    for st in students:
         result.append(f"Student №{st.student_id}: {st.first_name} {st.last_name}; Email: {st.email}")
    return "\n".join(result)
print(get_students_info())

def update_students_emails():
    students = Student.objects.all()
    for student in students:
        student.email = student.email.replace("university.com", "uni-students.com")
        student.save()
#
update_students_emails()
for student in Student.objects.all():
    print(student.email)

def truncate_students():
    students = Student.objects.all()
    students.delete()
# truncate_students()


