import curses
import time
import smilespcs


def get_command():
    with open("cmd.txt", "r") as f:
        return f.readline()


def add(screen, pcs, x, y):
    for i in range(0, len(pcs)):
        screen.addstr(y + i, x, pcs[i])


def draw(screen):
    cmd = get_command()
    curses.curs_set(0)
    screen.clear()
    x, y = screen.getmaxyx()
    x_offset = int(y / 2 - 19)
    y_offset = int(x / 2 - 6)
    add(screen, smilespcs.eye, x_offset + 0, y_offset + 0)
    add(screen, smilespcs.eye, x_offset + 19, y_offset + 0)
    if cmd == "stop":
        add(screen, smilespcs.mouth_closed, x_offset + 0, y_offset + 9)
    elif cmd == "say":
        add(screen, smilespcs.mouth_open, x_offset + 0, y_offset + 9)
    screen.refresh()


def main(scr):
    while True:
        draw(scr)
        time.sleep(0.1)


curses.wrapper(main)
