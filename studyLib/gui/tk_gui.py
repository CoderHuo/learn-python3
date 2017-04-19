#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox as msgbox

__author__ = 'Mr.Huo'


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.winfo_screenheight()
        self.pack()

        self._creatWidgets()

    def _creatWidgets(self):
        # 创建一个窗口 将其加入父容器
        self._helloLabel = Label(self, text='Hello World')
        self._helloLabel.pack()

        self._nameInput = Entry(self)
        self._nameInput.pack()

        self._helloButton = Button(self, text='Hello', command=self._hello)
        self._helloButton.pack()

        self._quitButton = Button(self, text='Quit', command=self.quit)
        self._quitButton.pack()

    def _hello(self):
        name = self._nameInput.get() or '芷瑄'
        msgbox.showinfo('Message', 'Hello %s' % name)


def main():
    app = Application()
    app.master.title('少华')
    # 可以随时增加其他窗口等
    app.myLabel = Label(text='少华')
    app.myLabel.pack()
    print(app.winfo_screenheight())
    for x in dir(app):
        print(x, ':', app.__getattribute__(x))
    app.mainloop()


if __name__ == '__main__':
    main()
