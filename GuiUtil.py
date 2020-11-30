import os 
import tkinter
import Commands
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
        self.menuButtons = {}
        self.loadMenu()
        

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

    def enterImageButton(self, parent, fileName, side, anchor, width, height, Command):
        AssetPath = str(os.path.dirname(os.path.realpath(__file__))) + '\\Assets\\' + fileName
        img = PIL.Image.open(AssetPath)
        img = img.resize((width, height), PIL.Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Button(parent, image=img, command = Command)
        panel.image = img
        panel.pack(side=side, anchor=anchor)
        return panel

    def removeMenu(self):
        #print(self.menuButtons)
        self.menuButtons['AddProject'].place_forget()
        self.menuButtons['AddHours'].place_forget()
        self.menuButtons['ViewProjects'].place_forget()

    def loadMenu(self):
        BackgroundImage = self.enterImage(self.master, 'Background.jpg', 'top', 'center', self.width, self.height)
        ExitImage = self.enterImageButton(self.master, 'ExitButton.png', 'top', 'center', int(self.width * .1), int(self.height * .1), Commands.ExitButton)
        ExitImage.place(relx=0.003, rely=0.01, anchor = 'nw')
        self.menuButtons['AddHours'] = self.enterImageButton(self.master, 'AddHours.png', 'top', 'center', int(self.width * .1), int(self.height * .1), Commands.ExitButton)
        self.menuButtons['AddHours'].place(relx=0.5, rely=0.5, anchor = 'center')
        self.menuButtons['ViewProjects'] = self.enterImageButton(self.master, 'ViewProjects.png', 'top', 'center', int(self.width * .1), int(self.height * .1), Commands.ExitButton)
        self.menuButtons['ViewProjects'].place(relx=0.5, rely=0.7, anchor = 'center')
        self.menuButtons['AddProject'] = self.enterImageButton(self.master, 'AddProject.png', 'top', 'center', int(self.width * .1), int(self.height * .1), self.removeMenu)
        self.menuButtons['AddProject'].place(relx=0.5, rely=0.3, anchor = 'center')
        #self.menuButtons['AddProject'].Command = Commands.removeMenu(self.menuButtons)