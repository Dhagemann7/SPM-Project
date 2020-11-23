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

    def createFrame(self, parent, side):
        frame = Frame(parent)
        frame.pack(side = side)
        return frame

    def editTitle(self, title):
        self.master.title(title)