# global lists to hold our data
students = []
courses = []
marks = []

# --- INPUT FUNCTIONS ---

def input_number_of_students():
    count = int(input("Enter number of students in class: "))
    return count

def input_student_information():
    print("\n--- Enter Student Info ---")
    id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    dob = input("Enter Student DoB (DD/MM/YYYY): ")
    
    # Create a dictionary for the student
    student = {
        "id": id,
        "name": name,
        "dob": dob
    }
    students.append(student)

def input_number_of_courses():
    count = int(input("\nEnter number of courses: "))
    return count

def input_course_information():
    print("\n--- Enter Course Info ---")
    id = input("Enter Course ID: ")
    name = input("Enter Course Name: ")
    
    # Create a dictionary for the course
    course = {
        "id": id,
        "name": name
    }
    courses.append(course)

def input_marks():
    print("\n--- Input Marks ---")
    # 1. Select a course
    list_courses()
    course_id = input("Enter the ID of the course to input marks for: ")
    
    # Check if course exists (optional logic, but good practice)
    # 2. Input marks for students in this course
    for s in students:
        mark = float(input(f"Enter mark for student {s['name']} (ID: {s['id']}): "))
        
        # We store marks as a dictionary with course_id, student_id, and the value
        mark_entry = {
            "course_id": course_id,
            "student_id": s["id"],
            "mark": mark
        }
        marks.append(mark_entry)

# --- LISTING FUNCTIONS ---

def list_courses():
    print("\n--- List of Courses ---")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")

def list_students():
    print("\n--- List of Students ---")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['dob']}")

def show_student_marks():
    print("\n--- Show Marks ---")
    list_courses()
    course_id = input("Enter Course ID to view marks: ")
    
    print(f"Marks for Course {course_id}:")
    for m in marks:
        if m["course_id"] == course_id:
            # Find student name for better display
            student_name = "Unknown"
            for s in students:
                if s["id"] == m["student_id"]:
                    student_name = s["name"]
                    break
            
            print(f"Student: {student_name}, Mark: {m['mark']}")

# --- MAIN PROGRAM MENU ---
# This runs the logic in a loop
if __name__ == "__main__":
    # 1. Ask for number of students
    num_students = input_number_of_students()
    for i in range(num_students):
        input_student_information()

    # 2. Ask for number of courses
    num_courses = input_number_of_courses()
    for i in range(num_courses):
        input_course_information()

    # 3. Simple Menu loop
    while True:
        print("\nOPTIONS:")
        print("1. List Courses")
        print("2. List Students")
        print("3. Input Marks for a Course")
        print("4. Show Marks for a Course")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == "1":
            list_courses()
        elif choice == "2":
            list_students()
        elif choice == "3":
            input_marks()
        elif choice == "4":
            show_student_marks()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")