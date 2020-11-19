import tkinter
from tkinter import *

class AppWindow(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

    def panelTest(self):
        pass
