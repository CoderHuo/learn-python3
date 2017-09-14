#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter

__author__ = 'Mr.Huo'


def _test():
    root = tkinter.Tk()
    text = "This is Tcl/Tk version %s" % tkinter.TclVersion
    text += "\nThis should be a cedilla: \xe7"
    label = tkinter.Label(root, text=text)
    label.pack()
    test = tkinter.Button(root, text="Click me!",
                          command=lambda root=root: root.test.configure(
                              text="[%s]" % root.test['text']))
    test.pack()
    root.test = test
    print(root.readprofile('tk_frame.py','tk'))
    quit = tkinter.Button(root, text="QUIT", command=root.destroy)
    quit.pack()
    root.withdraw()
    # The following three commands are needed so the window pops
    # up on top on Windows...
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()


def main():
    # root = tkinter.Tk()
    # root.mainloop()
    _test()


if __name__ == '__main__':
    main()
