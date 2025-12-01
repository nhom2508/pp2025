

class Student:
    def __init__(self):
        # ENCAPSULATION: 
        self._id = ""
        self._name = ""
        self._dob = ""

    # POLYMORPHISM: This method has the same name as in the Course class
    def input(self):
        self._id = input("Enter Student ID: ")
        self._name = input("Enter Student Name: ")
        self._dob = input("Enter Student DoB (DD/MM/YYYY): ")

    # POLYMORPHISM: Same method name, different behavior
    def list(self):
        print(f"ID: {self._id}, Name: {self._name}, DoB: {self._dob}")

    # Getter for ID (Helper for marks)
    def get_id(self):
        return self._id
    
    def get_name(self):
        return self._name


class Course:
    def __init__(self):
        self._id = ""
        self._name = ""

    # POLYMORPHISM: Same method name as Student
    def input(self):
        self._id = input("Enter Course ID: ")
        self._name = input("Enter Course Name: ")

    # POLYMORPHISM: Same method name as Student
    def list(self):
        print(f"ID: {self._id}, Name: {self._name}")

    def get_id(self):
        return self._id


class MarkManagement:
    def __init__(self):
        # attributes to store our lists of objects
        self.students = []
        self.courses = []
        self.marks = [] # We will store marks as dictionaries for simplicity

    def input_students(self):
        num = int(input("\nEnter number of students: "))
        for _ in range(num):
            # Create a Student OBJECT
            s = Student()
            s.input() # Call the object's method
            self.students.append(s)

    def input_courses(self):
        num = int(input("\nEnter number of courses: "))
        for _ in range(num):
            # Create a Course OBJECT
            c = Course()
            c.input()
            self.courses.append(c)

    def input_marks(self):
        print("\n--- Input Marks ---")
        self.list_courses()
        course_id = input("Enter Course ID to input marks for: ")
        
        # Verify course exists (simplified)
        if not any(c.get_id() == course_id for c in self.courses):
            print("Course not found.")
            return

        for s in self.students:
            mark = float(input(f"Enter mark for {s.get_name()} (ID: {s.get_id()}): "))
            # Store as simple dict data
            data = {
                "course_id": course_id,
                "student_id": s.get_id(),
                "mark": mark
            }
            self.marks.append(data)

    def list_students(self):
        print("\n--- List of Students ---")
        for s in self.students:
            s.list() # Using the Polymorphic method

    def list_courses(self):
        print("\n--- List of Courses ---")
        for c in self.courses:
            c.list() # Using the Polymorphic method

    def show_marks(self):
        print("\n--- Show Marks ---")
        self.list_courses()
        course_id = input("Enter Course ID to view: ")

        print(f"Marks for Course {course_id}:")
        for m in self.marks:
            if m["course_id"] == course_id:
                # Find student name
                student_name = "Unknown"
                for s in self.students:
                    if s.get_id() == m["student_id"]:
                        student_name = s.get_name()
                        break
                print(f"Student: {student_name}, Mark: {m['mark']}")


# --- MAIN DRIVER ---
if __name__ == "__main__":
    # Create the management system object
    school = MarkManagement()

    while True:
        print("\nOPTIONS:")
        print("1. Input Students")
        print("2. Input Courses")
        print("3. List Students")
        print("4. List Courses")
        print("5. Input Marks")
        print("6. Show Marks")
        print("7. Exit")
        
        choice = input("Select: ")
        
        if choice == "1":
            school.input_students()
        elif choice == "2":
            school.input_courses()
        elif choice == "3":
            school.list_students()
        elif choice == "4":
            school.list_courses()
        elif choice == "5":
            school.input_marks()
        elif choice == "6":
            school.show_marks()
        elif choice == "7":
            break
        else:
            print("Invalid")