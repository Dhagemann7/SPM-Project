import os
import tkinter
import sys
from tkinter import *
import ProjectUtil
from ProjectUtil import Project

def ExitButton():
    sys.exit()
    return

def removeMenu(buttons):
    print(buttons)
    buttons['AddHours'].place_forget() #AddHoursViewProjects
    #buttons['AddHours'].place_destroy()

def doNothing():
    pass

#def Writer(i, input):
#    projectwriter = Project()
#    projectwriter.editRow('Project', i, input)
#    return

def StringAdder(Stuff, Stuffinput):
    Stuff.append(Stuffinput)
    return
