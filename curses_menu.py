# -*- coding: utf-8 -*-

from os import system
import curses


def get_param(prompt_string):
    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, prompt_string)
    screen.refresh()
    input_str = screen.getstr(10, 10, 60)
    return str(input_str)


def execute_cmd(cmd_string):
    system("clear")
    a = system(cmd_string)
    print("")
    if a == 0:
        print("Command executed correctly")
    else:
        print("Command terminated with error")
    input("Press enter")
    print("")


x = 0

while x != ord('4'):
    screen = curses.initscr()

    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, "Please enter a number...")
    screen.addstr(4, 4, "1 - Add a user")  # have not implemented on OS X
    screen.addstr(5, 4, "2 - Login mysql")
    screen.addstr(6, 4, "3 - Show disk space")
    screen.addstr(7, 4, "4 - Exit")
    screen.refresh()

    x = screen.getch()

    if x== ord('1'):
        username = get_param("Enter the username")
        homedir = get_param("Enter the home directory, eg /home/name")
        groups = get_param("Enter comma-separated groups, eg adm, dialout, cdrom")
        shell = get_param("Enter the shell, eg /bin/bash:")
        curses.endwin()
        execute_cmd("pw useradd -d " + homedir + " -g 1000 -G " + groups + " -m -s " + shell + " " + username)

    if x == ord('2'):
        curses.endwin()
        execute_cmd("mysql -uroot -p")

    if x == ord('3'):
        curses.endwin()
        execute_cmd("df -h")

    curses.endwin()


