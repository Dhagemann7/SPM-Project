import os 
import tkinter
from tkinter import *
#Pillow is not included in standard library, must be installed to your python library first.
import PIL
from PIL import ImageTk, Image

class AppWindow(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.state('zoomed')
        self.pack()
        dimFrame = Frame(self.master)
        dimFrame.pack(fill = BOTH, expand = True)
        self.master.update()
        self.width = dimFrame.winfo_width()
        self.height = dimFrame.winfo_height()
        dimFrame.pack_forget()
        dimFrame.destroy()
        

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

    def enterImage(self, parent, fileName, side, anchor, width, height):
        AssetPath = str(os.path.dirname(os.path.realpath(__file__))) + '\\Assets\\' + fileName
        img = PIL.Image.open(AssetPath)
        img = img.resize((width, height), PIL.Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(parent, image = img)
        panel.image = img
        panel.pack(side = side, anchor = anchor)
        return panel
