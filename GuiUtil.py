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
        self.addprojectUI = {}
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

    def enterImageButtonTwoFunc(self, parent, fileName, side, anchor, width, height, Command, Command2):
        AssetPath = str(os.path.dirname(os.path.realpath(__file__))) + '\\Assets\\' + fileName
        img = PIL.Image.open(AssetPath)
        img = img.resize((width, height), PIL.Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Button(parent, image=img, command = Commands.sequence(Command, Command2))
        panel.image = img
        panel.pack(side=side, anchor=anchor)
        return panel

    def removeMenu(self):
        #print(self.menuButtons)
        self.menuButtons['AddProject'].place_forget()
        self.menuButtons['AddHours'].place_forget()
        self.menuButtons['ViewProjects'].place_forget()
        self.menuButtons['Exit'].place_forget()

    def loadMenu(self):

        BackgroundImage = self.enterImage(self.master, 'Background.jpg', 'top', 'center', self.width, self.height)
        self.menuButtons['Exit'] = self.enterImageButton(self.master, 'Exit.png', 'top', 'center', int(self.width * .1), int(self.height * .1), Commands.ExitButton)
        self.menuButtons['Exit'].place(relx=0.003, rely=0.01, anchor = 'nw')
        self.menuButtons['AddHours'] = self.enterImageButton(self.master, 'ViewHours.png', 'top', 'center', int(self.width * .1), int(self.height * .1), self.addHoursmenu)
        self.menuButtons['AddHours'].place(relx=0.5, rely=0.5, anchor = 'center')
        self.menuButtons['ViewProjects'] = self.enterImageButton(self.master, 'ViewProjects.png', 'top', 'center', int(self.width * .1), int(self.height * .1), self.addViewProject)
        self.menuButtons['ViewProjects'].place(relx=0.5, rely=0.7, anchor = 'center')
        self.menuButtons['AddProject'] = self.enterImageButton(self.master, 'AddProject.png', 'top', 'center', int(self.width * .1), int(self.height * .1), self.addprojectmenu)
        self.menuButtons['AddProject'].place(relx=0.5, rely=0.3, anchor = 'center')
        #self.menuButtons['AddProject'].Command = Commands.removeMenu(self.menuButtons)

    def addprojectmenu(self):

        self.removeMenu()
        self.addprojectUI['BackButtonProject'] = self.enterImageButtonTwoFunc(self.master, 'Back.png', 'top', 'center', int(self.width * .1), int(self.height * .1), self.removeprojectmenu, self.loadMenu)
        self.addprojectUI['BackButtonProject'].place(relx=0.003, rely=0.01, anchor = 'nw')

        self.addprojectUI['NameLabel'] = tkinter.Label(self.master, text = 'Project Name')
        self.addprojectUI['NameLabel'].place(relx=0.25, rely=0.45)

        self.addprojectUI['NameEntry'] = tkinter.Entry(self.master)
        self.addprojectUI['NameEntry'].place(relx=0.25, rely=0.5)

        self.addprojectUI['SaveProject'] = self.enterImageButton(self.master, 'SaveProject.png', 'top', 'center', int(self.width * .1), int(self.height * .1), Commands.ExitButton)
        self.addprojectUI['SaveProject'].place(relx=0.5, rely=0.9, anchor='center')



    def removeprojectmenu(self):

        self.addprojectUI['NameEntry'].place_forget()
        self.addprojectUI['NameLabel'].place_forget()
        self.addprojectUI['BackButtonProject'].place_forget()
        self.addprojectUI['SaveProject'].place_forget()

    def addHoursmenu(self):

        self.removeMenu()
        self.addprojectUI['BackButtonHours'] = self.enterImageButtonTwoFunc(self.master, 'Back.png', 'top', 'center',
                                                                       int(self.width * .1), int(self.height * .1),
                                                                       self.removehoursmenu, self.loadMenu)
        self.addprojectUI['BackButtonHours'].place(relx=0.003, rely=0.01, anchor='nw')



        self.addprojectUI['Addhours'] = self.enterImageButton(self.master, 'Submit.png', 'top', 'center',
                                                              int(self.width * .1), int(self.height * .1),
                                                              Commands.ExitButton)
        self.addprojectUI['Addhours'].place(relx=0.5, rely=0.9, anchor = 'center')

        self.addprojectUI['MainHoursLabel'] = tkinter.Label(self.master, text='Add daily hours for each task then submit.')
        self.addprojectUI['MainHoursLabel'].place(relx=0.5, rely=0.05, anchor = 'n')

        self.addprojectUI['ReqHours'] = tkinter.Label(self.master, text='Requirement Hours')
        self.addprojectUI['ReqHours'].place(relx=0.15, rely=0.45, anchor = 'w')

        self.addprojectUI['ReqEntry'] = tkinter.Entry(self.master)
        self.addprojectUI['ReqEntry'].place(relx=0.15, rely=0.5, anchor = 'w')

        return

    def removehoursmenu(self):

        self.addprojectUI['BackButtonHours'].place_forget()
        self.addprojectUI['Addhours'].place_forget()
        self.addprojectUI['MainHoursLabel'].place_forget()
        self.addprojectUI['ReqHours'].place_forget()
        self.addprojectUI['ReqEntry'].place_forget()

        return

    def addViewProject(self):

        self.removeMenu()

        self.addprojectUI['BackButtonView'] = self.enterImageButtonTwoFunc(self.master, 'Back.png', 'top',
                                                                            'center',
                                                                            int(self.width * .1), int(self.height * .1),
                                                                            self.removeViewProject, self.loadMenu)
        self.addprojectUI['BackButtonView'].place(relx=0.003, rely=0.01, anchor='nw')

        self.addprojectUI['EnterProject'] = tkinter.Label(self.master, text = 'Type in Project name to load.')
        self.addprojectUI['EnterProject'].place(relx=0.5, rely=.45)
        self.addprojectUI['LoadEntry'] = tkinter.Entry(self.master)
        self.addprojectUI['LoadEntry'].place(relx=0.5, rely=.5)
        self.addprojectUI['LoadProject'] = self.enterImageButton(self.master, 'LoadProject.png', 'top', 'center',
                                                              int(self.width * .1), int(self.height * .1), Commands.ExitButton)
        self.addprojectUI['LoadProject'].place(relx=0.5,rely=.9, anchor= 'center')

        return

    def removeViewProject(self):
        self.addprojectUI['BackButtonView'].place_forget()
        self.addprojectUI['EnterProject'].place_forget()
        self.addprojectUI['LoadEntry'].place_forget()
        self.addprojectUI['LoadProject'].place_forget()
        return






