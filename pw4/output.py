import curses

def draw_menu(stdscr, selected_idx, menu_items):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    title = "STUDENT MANAGEMENT (PW4 Modularized)"
    stdscr.addstr(0, w//2 - len(title)//2, title, curses.A_BOLD)

    for idx, item in enumerate(menu_items):
        x = w//2 - len(item)//2
        y = h//2 - len(menu_items)//2 + idx
        if idx == selected_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, item)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, item)
    stdscr.refresh()

def show_list_curses(stdscr, students):
    stdscr.clear()
    stdscr.addstr(1, 2, "--- STUDENTS SORTED BY GPA ---", curses.A_BOLD)
    r = 3
    for s in students:
        stdscr.addstr(r, 2, str(s))
        r += 1
    stdscr.addstr(r+1, 2, "Press any key to return...")
    stdscr.getch()

def show_list_text(students):
    print("\n--- RANKING ---")
    for s in students:
        print(s)