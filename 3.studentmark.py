import math
import numpy as np
import sys

try:
    import curses
    CURSES_AVAILABLE = True
except ImportError:
    CURSES_AVAILABLE = False

class Student:
    def __init__(self, name, id, dob):
        self.name = name
        self.id = id
        self.dob = dob
        self.marks = {} 
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

class Course:
    def __init__(self, name, id, credit):
        self.name = name
        self.id = id
        self.credit = credit

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

def curses_main(stdscr, school):
    curses.curs_set(0) 
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE) 

    menu_items = ["Add Student", "Add Course", "Add Marks", "List Students (Sorted by GPA)", "Exit"]
    current_row = 0

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        title = "STUDENT MANAGEMENT (Python 3.14 Compatible)"
        stdscr.addstr(0, w//2 - len(title)//2, title, curses.A_BOLD)

        for idx, row in enumerate(menu_items):
            x = w//2 - len(row)//2
            y = h//2 - len(menu_items)//2 + idx
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu_items) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            
            if current_row == 4: break 
            
           

def text_main(school):
    while True:
        print("\n--- TEXT MENU (Curses not available) ---")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Add Marks")
        print("4. List Students (Sorted by GPA)")
        print("5. Exit")
        choice = input("Select: ")

        if choice == "1":
            name = input("Name: ")
            sid = input("ID: ")
            dob = input("DoB: ")
            school.add_student(name, sid, dob)
        elif choice == "2":
            name = input("Course Name: ")
            cid = input("Course ID: ")
            cred = int(input("Credits: "))
            school.add_course(name, cid, cred)
        elif choice == "3":
            sid = input("Student ID: ")
            cid = input("Course ID: ")
            mark = float(input("Mark: "))
            school.add_mark(sid, cid, mark)
        elif choice == "4":
            school.sort_students()
            print("\n--- RANKING ---")
            for s in school.students:
                print(s)
        elif choice == "5":
            break


if __name__ == "__main__":
    school = SchoolSystem()
    
    if CURSES_AVAILABLE:
        try:
            curses.wrapper(lambda stdscr: curses_main(stdscr, school))
        except:
           
            text_main(school)
    else:
        print("WARNING: 'windows-curses' library not installed.")
        print("Running in standard Text Mode so you can check your logic.")
        text_main(school)