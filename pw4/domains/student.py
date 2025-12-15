import numpy as np

class Student:
    def __init__(self, name, id, dob):
        self.name = name
        self.id = id
        self.dob = dob
        self.marks = {} # Dictionary {course_id: mark}
        self.gpa = 0.0

    def calculate_gpa(self, courses):
        score_list = []
        credit_list = []
        
        for course in courses:
            if course.id in self.marks:
                score_list.append(self.marks[course.id])
                credit_list.append(course.credit)
        
        if len(score_list) > 0:
            np_scores = np.array(score_list)
            np_credits = np.array(credit_list)
            self.gpa = np.average(np_scores, weights=np_credits)
        else:
            self.gpa = 0.0

    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | GPA: {self.gpa:.2f}"