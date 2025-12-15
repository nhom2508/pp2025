import math
from .student import Student
from .course import Course

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, name, id, dob):
        self.students.append(Student(name, id, dob))

    def add_course(self, name, id, credit):
        self.courses.append(Course(name, id, credit))

    def add_mark(self, student_id, course_id, mark):
        rounded_mark = math.floor(mark * 10) / 10
        for s in self.students:
            if s.id == student_id:
                s.marks[course_id] = rounded_mark
                s.calculate_gpa(self.courses)
                return

    def sort_students(self):
        self.students.sort(key=lambda x: x.gpa, reverse=True)