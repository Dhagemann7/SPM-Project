import os 
import tkinter
import Commands
from tkinter import *
#Pillow is not included in standard library, must be installed to your python library first.
import PIL
from PIL import ImageTk, Image
import ProjectUtil
from ProjectUtil import Project

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
        self.addprojectUI['AddProject'].place_forget()
        self.addprojectUI['AddHours'].place_forget()
        self.addprojectUI['ViewProjects'].place_forget()
        self.addprojectUI['Exit'].place_forget()
        self.addprojectUI['AddRequirements'].place_forget()

    def loadMenu(self):

        BackgroundImage = self.enterImage(self.master, 'Background.jpg', 'top', 'center', self.width, self.height)
        self.addprojectUI['Exit'] = self.enterImageButton(self.master, 'Exit.png', 'top', 'center', int(self.width * .1), int(self.height * .1), Commands.ExitButton)
        self.addprojectUI['Exit'].place(relx=0.003, rely=0.01, anchor = 'nw')
        self.addprojectUI['AddRequirements'] = self.enterImageButton(self.master, 'AddRequirements.png', 'top', 'center', int(self.width * .1), int(self.height * .1), self.addRequirementsMenu)
        self.addprojectUI['AddRequirements'].place(relx=0.5, rely=0.4, anchor = 'center')
        self.addprojectUI['AddHours'] = self.enterImageButton(self.master, 'AddHours.png', 'top', 'center', int(self.width * .1), int(self.height * .1), self.addHoursmenu)
        self.addprojectUI['AddHours'].place(relx=0.5, rely=0.6, anchor = 'center')
        self.addprojectUI['ViewProjects'] = self.enterImageButton(self.master, 'ViewProjects.png', 'top', 'center', int(self.width * .1), int(self.height * .1), self.addViewProject)
        self.addprojectUI['ViewProjects'].place(relx=0.5, rely=0.8, anchor = 'center')
        self.addprojectUI['AddProject'] = self.enterImageButton(self.master, 'AddProject.png', 'top', 'center', int(self.width * .1), int(self.height * .1), self.addprojectmenu)
        self.addprojectUI['AddProject'].place(relx=0.5, rely=0.2, anchor = 'center')
        #self.addprojectUI['AddProject'].Command = Commands.removeMenu(self.addprojectUI)



    def addprojectmenu(self):

        self.removeMenu()
        self.addprojectUI['BackButtonProject'] = self.enterImageButtonTwoFunc(self.master, 'Back.png', 'top', 'center', int(self.width * .1), int(self.height * .1), self.removeprojectmenu, self.loadMenu)
        self.addprojectUI['BackButtonProject'].place(relx=0.003, rely=0.01, anchor = 'nw')

        self.addprojectUI['NameLabel'] = tkinter.Label(self.master, text = 'Project Name')
        self.addprojectUI['NameLabel'].place(relx=0.25, rely=0.35)

        self.addprojectUI['NameEntry'] = tkinter.Entry(self.master)
        self.addprojectUI['NameEntry'].place(relx=0.25, rely=0.4)

        self.addprojectUI['OwnerLabel'] = tkinter.Label(self.master, text = 'Project Owner')
        self.addprojectUI['OwnerLabel'].place(relx=0.45, rely=0.35)

        self.addprojectUI['OwnerEntry'] = tkinter.Entry(self.master)
        self.addprojectUI['OwnerEntry'].place(relx=0.45, rely=0.4)

        self.addprojectUI['MembersLabel'] = tkinter.Label(self.master, text = 'Project Members - Seperate by commas')
        self.addprojectUI['MembersLabel'].place(relx=0.65, rely=0.35)

        self.addprojectUI['MembersEntry'] = tkinter.Entry(self.master)
        self.addprojectUI['MembersEntry'].place(relx=0.65, rely=0.4)

        self.addprojectUI['DescriptionLabel'] = tkinter.Label(self.master, text = 'Project Description')
        self.addprojectUI['DescriptionLabel'].place(relx=0.25, rely=0.55)

        self.addprojectUI['DescriptionEntry'] = tkinter.Entry(self.master)
        self.addprojectUI['DescriptionEntry'].place(relx=0.25, rely=0.6)

        self.addprojectUI['RisksLabel'] = tkinter.Label(self.master, text = 'Project Risks - Seperate by commas')
        self.addprojectUI['RisksLabel'].place(relx=0.45, rely=0.55)

        self.addprojectUI['RisksEntry'] = tkinter.Entry(self.master)
        self.addprojectUI['RisksEntry'].place(relx=0.45, rely=0.6)

        self.addprojectUI['RiskStatusLabel'] = tkinter.Label(self.master, text = 'Project RiskStatus - Seperate by commas')
        self.addprojectUI['RiskStatusLabel'].place(relx=0.65, rely=0.55)

        self.addprojectUI['RiskStatusEntry'] = tkinter.Entry(self.master)
        self.addprojectUI['RiskStatusEntry'].place(relx=0.65, rely=0.6)
        self.addprojectUI['SaveProject'] = self.enterImageButton(self.master, 'SaveProject.png', 'top', 'center', int(self.width * .1), int(self.height * .1), Command = lambda : self.AddProject())
        self.addprojectUI['SaveProject'].place(relx=0.5, rely=0.9, anchor='center')

    def AddProject(self):
        newProj = Project()
        newProj.createFile(self.addprojectUI['NameEntry'].get(), self.addprojectUI['OwnerEntry'].get(), self.addprojectUI['MembersEntry'].get(), self.addprojectUI['DescriptionEntry'].get(), self.addprojectUI['RisksEntry'].get(), self.addprojectUI['RiskStatusEntry'].get())
        self.removeprojectmenu()
        self.loadMenu()
        #Commands.AddProject(self.addprojectUI['NameEntry'].get(), self.addprojectUI['OwnerEntry'].get(), self.addprojectUI['MembersEntry'].get(), self.addprojectUI['DescriptionEntry'].get(), self.addprojectUI['RisksEntry'].get(), self.addprojectUI['RiskStatusEntry'].get())


    def removeprojectmenu(self):

        self.addprojectUI['NameEntry'].place_forget()
        self.addprojectUI['NameLabel'].place_forget()
        self.addprojectUI['OwnerLabel'].place_forget()
        self.addprojectUI['OwnerEntry'].place_forget()
        self.addprojectUI['MembersLabel'].place_forget()
        self.addprojectUI['MembersEntry'].place_forget()
        self.addprojectUI['DescriptionLabel'].place_forget()
        self.addprojectUI['DescriptionEntry'].place_forget()
        self.addprojectUI['RisksLabel'].place_forget()
        self.addprojectUI['RisksEntry'].place_forget()
        self.addprojectUI['RiskStatusLabel'].place_forget()
        self.addprojectUI['RiskStatusEntry'].place_forget()
        self.addprojectUI['BackButtonProject'].place_forget()
        self.addprojectUI['SaveProject'].place_forget()

    def addRequirementsMenu(self):

        self.removeMenu()
        self.addprojectUI['BackButtonRequirements'] = self.enterImageButtonTwoFunc(self.master, 'Back.png', 'top', 'center',
                                                                       int(self.width * .1), int(self.height * .1),
                                                                       self.removerequirementsmenu, self.loadMenu)
        self.addprojectUI['BackButtonRequirements'].place(relx=0.003, rely=0.01, anchor='nw')



        self.addprojectUI['AddRequirements'] = self.enterImageButton(self.master, 'Submit.png', 'top', 'center',
                                                              int(self.width * .1), int(self.height * .1),
                                                              Command = lambda: self.addRequirements())
        self.addprojectUI['AddRequirements'].place(relx=0.5, rely=0.9, anchor = 'center')

        self.addprojectUI['RequirementsLabel'] = tkinter.Label(self.master, text='Add requirements, seperated by commas.')
        self.addprojectUI['RequirementsLabel'].place(relx=0.5, rely=0.05, anchor = 'n')

        self.addprojectUI['ProjectNameLabel'] = tkinter.Label(self.master, text='Project Name')
        self.addprojectUI['ProjectNameLabel'].place(relx=0.45, rely=0.25, anchor = 'w')
        
        self.addprojectUI['ProjectNameEntry'] = tkinter.Entry(self.master)
        self.addprojectUI['ProjectNameEntry'].place(relx=0.45, rely=0.3, anchor = 'w')

        self.addprojectUI['FunctionalRequirementsLabel'] = tkinter.Label(self.master, text='Functional Requirements')
        self.addprojectUI['FunctionalRequirementsLabel'].place(relx=0.45, rely=0.45, anchor = 'w')

        self.addprojectUI['FunctionalRequirementsEntry'] = tkinter.Entry(self.master)
        self.addprojectUI['FunctionalRequirementsEntry'].place(relx=0.45, rely=0.5, anchor = 'w')

        self.addprojectUI['NonFunctionalRequirementsLabel'] = tkinter.Label(self.master, text='NonFunctional Requirements')
        self.addprojectUI['NonFunctionalRequirementsLabel'].place(relx=0.45, rely=0.65, anchor = 'w')

        self.addprojectUI['NonFunctionalRequirementsEntry'] = tkinter.Entry(self.master)
        self.addprojectUI['NonFunctionalRequirementsEntry'].place(relx=0.45, rely=0.7, anchor = 'w')

    def addRequirements(self):
        newProj = Project()
        contents = newProj.readFile(self.addprojectUI['ProjectNameEntry'].get())
        functionalRequirementsList = []
        nonFunctionalRequirementsList = []
        if(self.addprojectUI['FunctionalRequirementsEntry'].get() == ''):
            pass
        elif(',' in self.addprojectUI['FunctionalRequirementsEntry'].get()):
            functionalRequirementsList = (self.addprojectUI['FunctionalRequirementsEntry'].get().split(','))
        else:
            functionalRequirementsList.append(self.addprojectUI['FunctionalRequirementsEntry'].get())
        if(self.addprojectUI['NonFunctionalRequirementsEntry'].get() == ''):
            pass
        elif(',' in self.addprojectUI['NonFunctionalRequirementsEntry'].get()):
            nonFunctionalRequirementsList = (self.addprojectUI['NonFunctionalRequirementsEntry'].get().split(','))
        else:
            nonFunctionalRequirementsList.append(self.addprojectUI['NonFunctionalRequirementsEntry'].get())
        if(len(functionalRequirementsList) != 0):
            for y in range(len(functionalRequirementsList)):
                found = False
                row = 0
                newRow = []
                for x in range(len(contents['rows'])):
                    if(contents['rows'][x][6] == '' and not found):
                        row = x
                        found = True
                        break
                    else:
                        pass
                if(found):
                    newRow = contents['rows'][row]
                    diff = 15 - len(newRow)
                    newRow[6] = functionalRequirementsList[y]
                    newProj.editRow(self.addprojectUI['ProjectNameEntry'].get(), row, newRow)
                else:
                    newRow.append('')
                    newRow.append('')
                    newRow.append('')
                    newRow.append('')
                    newRow.append('')
                    newRow.append('')
                    newRow.append(functionalRequirementsList[y])
                    newRow.append('')
                    newRow.append('')
                    newRow.append('')
                    newRow.append('')
                    newRow.append('')
                    newRow.append('')
                    newRow.append('')
                    newRow.append('')
                    newProj.addRow(self.addprojectUI['ProjectNameEntry'].get(), newRow)
        if(len(nonFunctionalRequirementsList) != 0):
            for y in range(len(nonFunctionalRequirementsList)):
                found = False
                row = 0
                newRow = []
                for x in range(len(contents['rows'])):
                    if(contents['rows'][x][7] == '' and not found):
                        row = x
                        found = True
                        break
                    else:
                        pass
                if(found):
                    newRow = contents['rows'][row]
                    newRow[7] = nonFunctionalRequirementsList[y]
                    newProj.editRow(self.addprojectUI['ProjectNameEntry'].get(), row, newRow)
                else:
                    newRow.append('')
                    newRow.append('')
                    newRow.append('')
                    newRow.append('')
                    newRow.append('')
                    newRow.append('')
                    newRow.append('')
                    newRow.append(nonFunctionalRequirementsList[y])
                    newRow.append('')
                    newRow.append('')
                    newRow.append('')
                    newRow.append('')
                    newRow.append('')
                    newRow.append('')
                    newRow.append('')
                    newProj.addRow(self.addprojectUI['ProjectNameEntry'].get(), newRow)
        self.removerequirementsmenu()

    def removerequirementsmenu(self):

        self.addprojectUI['BackButtonRequirements'].place_forget()
        self.addprojectUI['AddRequirements'].place_forget()
        self.addprojectUI['RequirementsLabel'].place_forget()
        self.addprojectUI['ProjectNameLabel'].place_forget()
        self.addprojectUI['ProjectNameEntry'].place_forget()
        self.addprojectUI['FunctionalRequirementsLabel'].place_forget()
        self.addprojectUI['FunctionalRequirementsEntry'].place_forget()
        self.addprojectUI['AddRequirements'].place_forget()
        self.addprojectUI['NonFunctionalRequirementsLabel'].place_forget()
        self.addprojectUI['NonFunctionalRequirementsEntry'].place_forget()
        self.loadMenu()
        return

    def addHoursmenu(self):

        self.removeMenu()
        self.addprojectUI['BackButtonHours'] = self.enterImageButtonTwoFunc(self.master, 'Back.png', 'top', 'center',
                                                                       int(self.width * .1), int(self.height * .1),
                                                                       self.removehoursmenu, self.loadMenu)
        self.addprojectUI['BackButtonHours'].place(relx=0.003, rely=0.01, anchor='nw')



        self.addprojectUI['Addhours'] = self.enterImageButton(self.master, 'Submit.png', 'top', 'center',
                                                              int(self.width * .1), int(self.height * .1),
                                                              Command = lambda: self.addHours())
        self.addprojectUI['Addhours'].place(relx=0.5, rely=0.9, anchor = 'center')

        self.addprojectUI['MainHoursLabel'] = tkinter.Label(self.master, text='Add weekly hours for each category then submit.')
        self.addprojectUI['MainHoursLabel'].place(relx=0.5, rely=0.05, anchor = 'n')

        self.addprojectUI['ProjectNameLabel'] = tkinter.Label(self.master, text='Project Name')
        self.addprojectUI['ProjectNameLabel'].place(relx=0.15, rely=0.35, anchor = 'w')
        
        self.addprojectUI['ProjectNameEntry'] = tkinter.Entry(self.master)
        self.addprojectUI['ProjectNameEntry'].place(relx=0.15, rely=0.4, anchor = 'w')

        self.addprojectUI['WeekNumberLabel'] = tkinter.Label(self.master, text='Week Number')
        self.addprojectUI['WeekNumberLabel'].place(relx=0.35, rely=0.35, anchor = 'w')

        self.addprojectUI['WeekNumberEntry'] = tkinter.Entry(self.master)
        self.addprojectUI['WeekNumberEntry'].place(relx=0.35, rely=0.4, anchor = 'w')

        self.addprojectUI['PersonHoursTotalLabel'] = tkinter.Label(self.master, text='Person Hours Total')
        self.addprojectUI['PersonHoursTotalLabel'].place(relx=0.55, rely=0.35, anchor = 'w')

        self.addprojectUI['PersonHoursTotalEntry'] = tkinter.Entry(self.master)
        self.addprojectUI['PersonHoursTotalEntry'].place(relx=0.55, rely=0.4, anchor = 'w')

        self.addprojectUI['RequirementsAnalysisLabel'] = tkinter.Label(self.master, text='Requirements Analysis Hours')
        self.addprojectUI['RequirementsAnalysisLabel'].place(relx=0.75, rely=0.35, anchor = 'w')

        self.addprojectUI['RequirementsAnalysisEntry'] = tkinter.Entry(self.master)
        self.addprojectUI['RequirementsAnalysisEntry'].place(relx=0.75, rely=0.4, anchor = 'w')

        self.addprojectUI['DesigningLabel'] = tkinter.Label(self.master, text='Designing Hours')
        self.addprojectUI['DesigningLabel'].place(relx=0.15, rely=0.55, anchor = 'w')

        self.addprojectUI['DesigningEntry'] = tkinter.Entry(self.master)
        self.addprojectUI['DesigningEntry'].place(relx=0.15, rely=0.6, anchor = 'w')

        self.addprojectUI['CodingLabel'] = tkinter.Label(self.master, text='Coding Hours')
        self.addprojectUI['CodingLabel'].place(relx=0.35, rely=0.55, anchor = 'w')

        self.addprojectUI['CodingEntry'] = tkinter.Entry(self.master)
        self.addprojectUI['CodingEntry'].place(relx=0.35, rely=0.6, anchor = 'w')

        self.addprojectUI['TestingLabel'] = tkinter.Label(self.master, text='Testing Hours')
        self.addprojectUI['TestingLabel'].place(relx=0.55, rely=0.55, anchor = 'w')

        self.addprojectUI['TestingEntry'] = tkinter.Entry(self.master)
        self.addprojectUI['TestingEntry'].place(relx=0.55, rely=0.6, anchor = 'w')

        self.addprojectUI['ProjectManagementLabel'] = tkinter.Label(self.master, text='Project Management Hours')
        self.addprojectUI['ProjectManagementLabel'].place(relx=0.75, rely=0.55, anchor = 'w')
        
        self.addprojectUI['ProjectManagementEntry'] = tkinter.Entry(self.master)
        self.addprojectUI['ProjectManagementEntry'].place(relx=0.75, rely=0.6, anchor = 'w')
    
    def addHours(self):
        newProj = Project()
        contents = newProj.readFile(self.addprojectUI['ProjectNameEntry'].get())
        hourList = []
        if(self.addprojectUI['WeekNumberEntry'].get() == ''):
            hourList.append(0)
        else:
            hourList.append(self.addprojectUI['WeekNumberEntry'].get())
        if(self.addprojectUI['PersonHoursTotalEntry'].get() == ''):
            hourList.append(0)
        else:
            hourList.append(self.addprojectUI['PersonHoursTotalEntry'].get())
        if(self.addprojectUI['RequirementsAnalysisEntry'].get() == ''):
            hourList.append(0)
        else:
            hourList.append(self.addprojectUI['RequirementsAnalysisEntry'].get())
        if(self.addprojectUI['DesigningEntry'].get() == ''):
            hourList.append(0)
        else:
            hourList.append(self.addprojectUI['DesigningEntry'].get())
        if(self.addprojectUI['CodingEntry'].get() == ''):
            hourList.append(0)
        else:
            hourList.append(self.addprojectUI['CodingEntry'].get())
        if(self.addprojectUI['TestingEntry'].get() == ''):
            hourList.append(0)
        else:
            hourList.append(self.addprojectUI['TestingEntry'].get())
        if(self.addprojectUI['TestingEntry'].get() == ''):
            hourList.append(0)
        else:
            hourList.append(self.addprojectUI['TestingEntry'].get())
        found = False
        row = 0
        newRow = []
        for x in range(len(contents['rows'])):
            if(contents['rows'][x][8] == '' and not found):
                row = x
                found = True
                break
            else:
                pass
        if(found):
            newRow = contents['rows'][row]
            diff = 15 - len(newRow)
            for x in range(diff):
                newRow.append('')
            newRow[8] = hourList[0]
            newRow[9] = hourList[1]
            newRow[10] = hourList[2]
            newRow[11] = hourList[3]
            newRow[12] = hourList[4]
            newRow[13] = hourList[5]
            newRow[14] = hourList[6]
            newProj.editRow(self.addprojectUI['ProjectNameEntry'].get(), row, newRow)
        else:
            newRow.append('')
            newRow.append('')
            newRow.append('')
            newRow.append('')
            newRow.append('')
            newRow.append('')
            newRow.append('')
            newRow.append('')
            newRow.append(hourList[0])
            newRow.append(hourList[1])
            newRow.append(hourList[2])
            newRow.append(hourList[3])
            newRow.append(hourList[4])
            newRow.append(hourList[5])
            newRow.append(hourList[6])
            newProj.addRow(self.addprojectUI['ProjectNameEntry'].get(), newRow)
        self.removehoursmenu()
        return

    def removehoursmenu(self):

        self.addprojectUI['BackButtonHours'].place_forget()
        self.addprojectUI['Addhours'].place_forget()
        self.addprojectUI['MainHoursLabel'].place_forget()
        self.addprojectUI['ProjectNameLabel'].place_forget()
        self.addprojectUI['ProjectNameEntry'].place_forget()
        self.addprojectUI['WeekNumberLabel'].place_forget()
        self.addprojectUI['WeekNumberEntry'].place_forget()
        self.addprojectUI['PersonHoursTotalLabel'].place_forget()
        self.addprojectUI['PersonHoursTotalEntry'].place_forget()
        self.addprojectUI['RequirementsAnalysisLabel'].place_forget()
        self.addprojectUI['RequirementsAnalysisEntry'].place_forget()
        self.addprojectUI['DesigningLabel'].place_forget()
        self.addprojectUI['DesigningEntry'].place_forget()
        self.addprojectUI['CodingLabel'].place_forget()
        self.addprojectUI['CodingEntry'].place_forget()
        self.addprojectUI['TestingLabel'].place_forget()
        self.addprojectUI['TestingEntry'].place_forget()
        self.addprojectUI['ProjectManagementLabel'].place_forget()
        self.addprojectUI['ProjectManagementEntry'].place_forget()
        self.loadMenu()
        return

    def addViewProject(self):

        self.removeMenu()

        self.addprojectUI['BackButtonView'] = self.enterImageButtonTwoFunc(self.master, 'Back.png', 'top',
                                                                            'center',
                                                                            int(self.width * .1), int(self.height * .1),
                                                                            self.removeViewProject, self.loadMenu)
        self.addprojectUI['BackButtonView'].place(relx=0.003, rely=0.01, anchor='nw')

        self.addprojectUI['EnterProject'] = tkinter.Label(self.master, text = 'Type in Project name to load.')
        self.addprojectUI['EnterProject'].place(relx=0.5, rely=.45, anchor = 'center')
        self.addprojectUI['LoadEntry'] = tkinter.Entry(self.master)
        self.addprojectUI['LoadEntry'].place(relx=0.5, rely=.5, anchor = 'center')
        self.addprojectUI['LoadProject'] = self.enterImageButton(self.master, 'LoadProject.png', 'top', 'center',
                                                              int(self.width * .1), int(self.height * .1), Command = lambda: self.viewProject())
        self.addprojectUI['LoadProject'].place(relx=0.5,rely=.9, anchor= 'center')
        return

    def viewProject(self):
        self.addprojectUI['BackButtonView'] = self.enterImageButtonTwoFunc(self.master, 'Back.png', 'top',
                                                                            'center',
                                                                            int(self.width * .1), int(self.height * .1),
                                                                            self.removeViewProject, self.loadMenu)
        self.addprojectUI['BackButtonView'].place(relx=0.003, rely=0.01, anchor='nw')

        newProj = Project()
        self.contents = newProj.readFile(self.addprojectUI['LoadEntry'].get())

        widths = [0, 0.09, 0.175, 0.28, 0.43, 0.59, 0.65, 0.71, 0.77, 0.83, 0.89, 0.95]
        self.addprojectUI['EnterProject'].place_forget()
        self.addprojectUI['LoadEntry'].place_forget()
        self.addprojectUI['LoadProject'].place_forget()

        self.addprojectUI['ProjectName'] = tkinter.Label(self.master, text = 'Project Name: ' + self.contents['rows'][1][0])
        self.addprojectUI['ProjectName'].place(relx=0.15, rely=.03, anchor = 'w')

        self.addprojectUI['ProjectDescription'] = tkinter.Label(self.master, text = 'Project Description: ' + self.contents['rows'][1][3])
        self.addprojectUI['ProjectDescription'].place(relx=0.5, rely=.03, anchor = 'w')

        self.addprojectUI['ProjectOwner'] = tkinter.Label(self.master, text = 'Project Owner: ' + self.contents['rows'][1][1])
        self.addprojectUI['ProjectOwner'].place(relx=0.85, rely=.03, anchor = 'w')


        self.addprojectUI['MembersTitle'] = tkinter.Label(self.master, text = 'Members')
        self.addprojectUI['MembersTitle'].place(relx=widths[0], rely=.17, anchor = 'w')

        self.addprojectUI['RisksTitle'] = tkinter.Label(self.master, text = 'Risks')
        self.addprojectUI['RisksTitle'].place(relx=widths[1], rely=.17, anchor = 'w')
        
        self.addprojectUI['RiskStatusTitle'] = tkinter.Label(self.master, text = 'Risk\nStatus')
        self.addprojectUI['RiskStatusTitle'].place(relx=widths[2], rely=.17, anchor = 'w')
        
        self.addprojectUI['FunctionalRequirementsTitle'] = tkinter.Label(self.master, text = 'Functional\nRequirements')
        self.addprojectUI['FunctionalRequirementsTitle'].place(relx=widths[3], rely=.17, anchor = 'w')
        
        self.addprojectUI['NonFunctionalRequirementsTitle'] = tkinter.Label(self.master, text = 'NonFunctional\nRequirements')
        self.addprojectUI['NonFunctionalRequirementsTitle'].place(relx=widths[4], rely=.17, anchor = 'w')
        
        self.addprojectUI['WeekNumberTitle'] = tkinter.Label(self.master, text = 'Week\nNumber')
        self.addprojectUI['WeekNumberTitle'].place(relx=widths[5], rely=.17, anchor = 'w')
        
        self.addprojectUI['PersonHoursTotalTitle'] = tkinter.Label(self.master, text = 'Person\nHours\nTotal')
        self.addprojectUI['PersonHoursTotalTitle'].place(relx=widths[6], rely=.17, anchor = 'w')
        
        
        self.addprojectUI['DesigningHoursTitle'] = tkinter.Label(self.master, text = 'Designing\nHours')
        self.addprojectUI['DesigningHoursTitle'].place(relx=widths[8], rely=.17, anchor = 'w')

        self.addprojectUI['CodingHoursTitle'] = tkinter.Label(self.master, text = 'Coding\nHours')
        self.addprojectUI['CodingHoursTitle'].place(relx=widths[9], rely=.17, anchor = 'w')
        
        self.addprojectUI['TestingHoursTitle'] = tkinter.Label(self.master, text = 'Testing\nHours')
        self.addprojectUI['TestingHoursTitle'].place(relx=widths[10], rely=.17, anchor = 'w')
        
        self.addprojectUI['ProjectManagementTitle'] = tkinter.Label(self.master, text = 'Project\nManagement\nHours')
        self.addprojectUI['ProjectManagementTitle'].place(relx=widths[11], rely=.17, anchor = 'w')

        self.addprojectUI['RequirementsAnalysisHoursTitle'] = tkinter.Label(self.master, text = 'Requirements\nAnalysis\nHours')
        self.addprojectUI['RequirementsAnalysisHoursTitle'].place(relx=widths[7], rely=.17, anchor = 'w')

        self.memberLabels = []
        self.riskLabels = []
        self.riskStatusLabels = []
        self.functionalRequirementLabels = []
        self.nonFunctionalRequirementLabels = []
        self.weekNumberLabels = []
        self.personHourLabels = []
        self.requirementsAnalysisLabels = []
        self.designingHoursLabels = []
        self.codingHoursLabels = []
        self.testingHoursLabels = []
        self.projectManagementLabels = []
        for x in range(len(self.contents['rows'])):
            y = len(self.contents['rows']) - x - 1
            if(y == 0):
                pass
            else:
                diff = 14 - len(self.contents['rows'][y])
                
                for x in range(diff):
                    self.contents['rows'][y].append('')
                if(self.contents['rows'][y][2] == ''):
                    pass
                else:
                    label = tkinter.Label(self.master, text = self.contents['rows'][y][2])
                    label.place(relx=widths[0], rely=(.17+(y*.05)), anchor = 'w')
                    self.memberLabels.append(label)
                if(self.contents['rows'][y][3] == ''):
                    pass
                else:
                    label = tkinter.Label(self.master, text = self.contents['rows'][y][3])
                    label.place(relx=widths[1], rely=(.17+(y*.05)), anchor = 'w')
                    self.riskLabels.append(label)
                if(self.contents['rows'][y][4] == ''):
                    pass
                else:
                    label = tkinter.Label(self.master, text = self.contents['rows'][y][4])
                    label.place(relx=widths[2], rely=(.17+(y*.05)), anchor = 'w')
                    self.riskStatusLabels.append(label)
                if(self.contents['rows'][y][5] == ''):
                    pass
                else:
                    label = tkinter.Label(self.master, text = self.contents['rows'][y][5])
                    label.place(relx=widths[3], rely=(.17+(y*.05)), anchor = 'w')
                    self.functionalRequirementLabels.append(label)
                if(self.contents['rows'][y][6] == ''):
                    pass
                else:
                    label = tkinter.Label(self.master, text = self.contents['rows'][y][6])
                    label.place(relx=widths[4], rely=(.17+(y*.05)), anchor = 'w')
                    self.nonFunctionalRequirementLabels.append(label)
                if(self.contents['rows'][y][7] == ''):
                    pass
                else:
                    label = tkinter.Label(self.master, text = self.contents['rows'][y][7])
                    label.place(relx=widths[5], rely=(.17+(y*.05)), anchor = 'w')
                    self.weekNumberLabels.append(label)
                if(self.contents['rows'][y][8] == ''):
                    pass
                else:
                    label = tkinter.Label(self.master, text = self.contents['rows'][y][8])
                    label.place(relx=widths[6], rely=(.17+(y*.05)), anchor = 'w')
                    self.personHourLabels.append(label)
                if(self.contents['rows'][y][9] == ''):
                    pass
                else:
                    label = tkinter.Label(self.master, text = self.contents['rows'][y][9])
                    label.place(relx=widths[7], rely=(.17+(y*.05)), anchor = 'w')
                    self.requirementsAnalysisLabels.append(label)
                if(self.contents['rows'][y][10] == ''):
                    pass
                else:
                    label = tkinter.Label(self.master, text = self.contents['rows'][y][10])
                    label.place(relx=widths[8], rely=(.17+(y*.05)), anchor = 'w')
                    self.designingHoursLabels.append(label)
                if(self.contents['rows'][y][11] == ''):
                    pass
                else:
                    label = tkinter.Label(self.master, text = self.contents['rows'][y][11])
                    label.place(relx=widths[9], rely=(.17+(y*.05)), anchor = 'w')
                    self.codingHoursLabels.append(label)
                if(self.contents['rows'][y][12] == ''):
                    pass
                else:
                    label = tkinter.Label(self.master, text = self.contents['rows'][y][12])
                    label.place(relx=widths[10], rely=(.17+(y*.05)), anchor = 'w')
                    self.testingHoursLabels.append(label)
                if(self.contents['rows'][y][13] == ''):
                    pass
                else:
                    label = tkinter.Label(self.master, text = self.contents['rows'][y][13])
                    label.place(relx=widths[11], rely=(.17+(y*.05)), anchor = 'w')
                    self.projectManagementLabels.append(label)

        self.allLabels = []
        self.allLabels.append(self.riskLabels)
        self.allLabels.append(self.riskStatusLabels)
        self.allLabels.append(self.functionalRequirementLabels)
        self.allLabels.append(self.weekNumberLabels)
        self.allLabels.append(self.personHourLabels)
        self.allLabels.append(self.requirementsAnalysisLabels)
        self.allLabels.append(self.designingHoursLabels)
        self.allLabels.append(self.codingHoursLabels)
        self.allLabels.append(self.testingHoursLabels)
        self.allLabels.append(self.projectManagementLabels)
        


    def removeViewProject(self):
        self.addprojectUI['BackButtonView'].place_forget()
        self.addprojectUI['EnterProject'].place_forget()
        self.addprojectUI['LoadEntry'].place_forget()
        self.addprojectUI['LoadProject'].place_forget()
        self.addprojectUI['ProjectName'].place_forget()
        self.addprojectUI['ProjectDescription'].place_forget()
        self.addprojectUI['ProjectOwner'].place_forget()
        self.addprojectUI['MembersTitle'].place_forget()
        self.addprojectUI['RisksTitle'].place_forget()
        self.addprojectUI['RiskStatusTitle'].place_forget()
        self.addprojectUI['FunctionalRequirementsTitle'].place_forget()
        self.addprojectUI['NonFunctionalRequirementsTitle'].place_forget()
        self.addprojectUI['WeekNumberTitle'].place_forget()
        self.addprojectUI['PersonHoursTotalTitle'].place_forget()
        self.addprojectUI['DesigningHoursTitle'].place_forget()
        self.addprojectUI['CodingHoursTitle'].place_forget()
        self.addprojectUI['TestingHoursTitle'].place_forget()
        self.addprojectUI['ProjectManagementTitle'].place_forget()
        self.addprojectUI['RequirementsAnalysisHoursTitle'].place_forget()
        for x in range(len(self.allLabels)):
            for y in range(len(self.allLabels[x])):
                self.allLabels[x][y].place_forget()
        self.loadMenu()
        return






