# -*- coding: utf-8 -*-

from tkinter import *


root = Tk()


def key(event):
    print("pressed", repr(event.char))


def callback(event):
    print("clicked at", event.x, event.y)


frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()
frame.focus_set()  # Must have, or the event Key can not work.

root.mainloop()


