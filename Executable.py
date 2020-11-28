import tkinter
import GuiUtil
import Commands
from GuiUtil import AppWindow
from tkinter import Tk
#For some reason, JUST importing this module makes the maximize function in Tkinter use the correct screen resolution.
import pyautogui
import csv
import ProjectUtil
from ProjectUtil import Project
#This will act as the main for the program.

#To my understanding, this line as well as mainloop(At the end of main) bookend the program main.
#The information between these two will be run in a loop.
mainWindow = tkinter.Tk()

#Values
risk1 = ''
risk2 = ''
riskinput1 = ''
riskinput2 = ''

#This initializes the GuiUtil class, most functions that interact with tkinter should be clustered in there as functions.
App = AppWindow(master=mainWindow)
App.editTitle('Project Tracker')

#Here's an example of how to put in things into the window.
risk1label = tkinter.Label(mainWindow, text = 'Risk 1')
risk1label.place(relx=0.45, rely=0.48, anchor='n')
risk1Entry = tkinter.Entry(mainWindow, textvariable=riskinput1)
risk1Entry.place(relx=0.45, rely=0.5, anchor='n')

risk2label = tkinter.Label(mainWindow, text = 'Risk 2')
risk2label.place(relx=0.65, rely=0.48, anchor='n')
risk2Entry = tkinter.Entry(mainWindow, textvariable=riskinput2)
risk2Entry.place(relx=0.65, rely=0.5, anchor='n')

ExitImage = App.enterImageButton(mainWindow, 'Temp Button-1.png', 'top', 'nw', 200, 100, Commands.ExitButton)
members = ['Dave', 'Haiden', 'Kyleel', 'Caleb']
risks = [risk1, risk2]
riskStatus = ['riskstatus1', 'riskstatus2']
requirements = ['requirement1', 'requirement2', 'requirement3']
Project1 = Project(name = 'tempFileName', owner = 'Dave', description = 'description', members = members, risks = risks, riskStatus = riskStatus, requirements = requirements)

App.mainloop()