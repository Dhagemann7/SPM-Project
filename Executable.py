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


first = True
#To my understanding, this line as well as mainloop(At the end of main) bookend the program main.
#The information between these two will be run in a loop.
mainWindow = tkinter.Tk()
#App = AppWindow(master=mainWindow)
if(first):
    App = AppWindow(master = mainWindow)
    App.editTitle('Project Tracker')
    first = False
#Values
#risk1 = ''
#risk2 = ''
#riskinput1 = ''
#riskinput2 = ''

#Arrays
#Risks = ['']
#Members = ['']
#RiskStatus = ['']
#Requirements = ['', '']

#This initializes the GuiUtil class, most functions that interact with tkinter should be clustered in there as functions.



#Here's an example of how to put in things into the window.

#riskslabel = tkinter.Label(mainWindow, text = 'Risk 1')
#riskslabel.place(relx=0.45, rely=0.48, anchor='n')
#risksEntry = tkinter.Entry(mainWindow)
#risksEntry.place(relx=0.45, rely=0.5, anchor='n')
#risksButton = tkinter.Button(mainWindow, text = 'Submit', command = Commands.StringAdder(Risks, risksEntry.get()))
#risksButton.place(relx = 0.45, rely = .55, anchor = 'n')


#projectfile = Project()
#projectfile.createFile('Project', 'Caleb', Members, '', Risks, RiskStatus, Requirements, '', '','', '', '', '')

App.mainloop()

