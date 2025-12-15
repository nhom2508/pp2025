import curses

def get_input_curses(stdscr, prompt, y, x):
    stdscr.addstr(y, x, prompt)
    curses.echo()
    user_input = stdscr.getstr(y, x + len(prompt)).decode('utf-8')
    curses.noecho()
    return user_input

def get_input_text(prompt):
    return input(prompt)