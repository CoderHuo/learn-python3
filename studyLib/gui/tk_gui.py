#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox as msgbox

__author__ = 'Mr.Huo'


class Application(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.pack()
        self.winfo_geometry()
        self._creatWidgets()
        # Frame如果设置大小的话，只有当使用了pack_propagate(0)或者grid_propagate(0)之后（width,height)才起作用，
        # 而且调用前Frame要pack或者grid了
        self.pack_propagate(0)
        print(self.pack_slaves())

    def _creatWidgets(self):
        # 创建一个窗口 将其加入父容器

        self._nameInput = Entry(self)
        self._nameInput.pack()

        self._helloButton = Button(self, text='Hello', command=self._hello)
        self._helloButton.pack()

        self._quitButton = Button(self, text='Quit', command=self.quit)
        self._quitButton.pack()

        self._scale = Scale(self, orient=HORIZONTAL, command=self._resize)
        self._scale.pack()

        self._helloLabel = Label(self, text='Hello World')
        self._helloLabel.pack()

    def _resize(self, ev=None):
        self._helloLabel.config(font='Helvetica -%d bold' % self._scale.get())

    def _hello(self):
        name = self._nameInput.get() or '芷瑄'
        msgbox.showinfo('Message', 'Hello %s' % name)


def main():
    app = Application(width=800, height=600)
    app.master.title('Hello World')
    # 可以随时增加其他窗口等
    app.myLabel = Label(text='Hello World1')
    app.myLabel.pack()
    print(app.winfo_screenheight())
    print(app.pack_slaves())
    app.mainloop()


if __name__ == '__main__':
    main()
