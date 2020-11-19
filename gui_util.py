import tkinter
from tkinter import *

class AppWindow(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.state('zoomed')
        self.pack()

    def getScreenSize(self):
        screenDimensions = {
            "height": self.winfo_screenheight(),
            "width": self.winfo_screenwidth()
        }
        return screenDimensions

    def createFrame(self, parent, side, h, w, bg):
        frame = Frame(parent, height = h, width = w, bg = bg)
        frame.pack(side = side)
        return frame