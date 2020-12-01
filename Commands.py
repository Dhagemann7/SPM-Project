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
    buttons['AddHours'].place_forget()
    return

def AddProject(name,owner,members,description):
    #create Project object from inputs (confirm button) -> go to project view
        #Project Name
        #Project Owner
        #Project Team Members
        #Project Description

    #go to project view

    return

def AddRisks(name,status):
    #adds risks to project (confirm button)
        #Risk Name
        #Risk Status

    #return to project view

    return

def AddRequirements(functional,nonfunctional):
    #add requirements to project (confirm button) -> 
        #Functional Requirements
        #Non-Functional Requirements

    # return to project view

    return

def AddHours(week,requirementsHours,designHours,codingHours,testingHours,projManagementHours):
    #add hours to project (confirm button)
        #Week Number
        #Requirements Analysis Hours
        #Design Hours
        #Coding Hours
        #Testing Hours
        #Project Management Hours

    #return to project view

    return

#def Writer(i, input):
#    projectwriter = Project()
#    projectwriter.editRow('Project', i, input)
#    return

def StringAdder(Stuff, Stuffinput):
    Stuff.append(Stuffinput)
    return
