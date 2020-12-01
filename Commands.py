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

def AddProject():
    #removeMenu(buttons) - To Remove Main Menu

    #create input fields
        #Project Name
        #Project Owner
        #Project Team Members
        #Project Description
        #Project Risks/Risk Status

    #get input from fields

    #create Project object from inputs

    return

def AddRequirements():
    #removeMenu(buttons) - To Remove Main Menu

    #create input fields
        #Functional Requirements
        #Non-Functional Requirements

    #get input from fields

    #add requirements to project

    return

def AddHours():
    #removeMenu(buttons) - To Remove Main Menu

    #create input fields
        #Week #
        #Requirements Analysis Hours
        #Design Hours
        #Coding Hours
        #Testing Hours
        #Project Management Hours

    #get input from fields

    #add week to project

    return

def ViewProject():
    #removeMenu(buttons) - To Remove Main Menu

    #display base project info + requirements

    return

def ViewHours():
    #removeMenu(buttons) - To Remove Main Menu

    #display project hours organized by type

    return



#def Writer(i, input):
#    projectwriter = Project()
#    projectwriter.editRow('Project', i, input)
#    return

def StringAdder(Stuff, Stuffinput):
    Stuff.append(Stuffinput)
    return
