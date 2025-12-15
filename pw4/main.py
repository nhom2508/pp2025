import sys
# Import from our own modules
from domains.school import SchoolSystem
import input as ui_in
import output as ui_out

# Check for curses support (Since you are on Python 3.14 Windows)
try:
    import curses
    CURSES_AVAILABLE = True
except ImportError:
    CURSES_AVAILABLE = False

def curses_main(stdscr, school):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    menu_items = ["Add Student", "Add Course", "Add Marks", "List Students", "Exit"]
    current_row = 0

    while True:
        ui_out.draw_menu(stdscr, current_row, menu_items)
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu_items) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            if current_row == 0:
                n = ui_in.get_input_curses(stdscr, "Name: ", 2, 2)
                i = ui_in.get_input_curses(stdscr, "ID: ", 3, 2)
                d = ui_in.get_input_curses(stdscr, "DoB: ", 4, 2)
                school.add_student(n, i, d)
            elif current_row == 1:
                n = ui_in.get_input_curses(stdscr, "Course: ", 2, 2)
                i = ui_in.get_input_curses(stdscr, "ID: ", 3, 2)
                try:
                    c = int(ui_in.get_input_curses(stdscr, "Credit: ", 4, 2))
                    school.add_course(n, i, c)
                except: pass
            elif current_row == 2:
                s = ui_in.get_input_curses(stdscr, "Student ID: ", 2, 2)
                c = ui_in.get_input_curses(stdscr, "Course ID: ", 3, 2)
                try:
                    m = float(ui_in.get_input_curses(stdscr, "Mark: ", 4, 2))
                    school.add_mark(s, c, m)
                except: pass
            elif current_row == 3:
                school.sort_students()
                ui_out.show_list_curses(stdscr, school.students)
            elif current_row == 4:
                break

def text_main(school):
    while True:
        print("\n--- TEXT MENU (No Curses) ---")
        print("1. Add Student\n2. Add Course\n3. Add Marks\n4. List Students\n5. Exit")
        choice = ui_in.get_input_text("Select: ")
        
        if choice == "1":
            school.add_student(ui_in.get_input_text("Name: "), ui_in.get_input_text("ID: "), ui_in.get_input_text("DoB: "))
        elif choice == "2":
            try:
                school.add_course(ui_in.get_input_text("Name: "), ui_in.get_input_text("ID: "), int(ui_in.get_input_text("Credit: ")))
            except: pass
        elif choice == "3":
            try:
                school.add_mark(ui_in.get_input_text("Sid: "), ui_in.get_input_text("Cid: "), float(ui_in.get_input_text("Mark: ")))
            except: pass
        elif choice == "4":
            school.sort_students()
            ui_out.show_list_text(school.students)
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
        text_main(school)