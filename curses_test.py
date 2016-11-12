# -*- coding: utf-8 -*-

import curses


stdscr = curses.initscr()


def display_info(str, x, y, colorpair=2):
    global stdscr
    stdscr.addstr(y, x, str, curses.color_pair(colorpair))
    stdscr.refresh()


def get_ch_and_continue():
    global stdscr
    stdscr.nodelay(0)
    ch = stdscr.getch()
    stdscr.nodelay(1)
    return True


def set_win():
    global stdscr
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.cbreak()
    stdscr.nodelay(1)


def unset_win():
    global stdscr
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()


if __name__ == '__main__':
    try:
        set_win()
        display_info('Hola, curses!', 0, 5)
        display_info('Press any key to continue...', 0, 10)
        get_ch_and_continue()
    except Exception as e:
        raise e
    finally:
        unset_win()


