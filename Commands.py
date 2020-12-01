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

    #get input from fields

    #create Project object from inputs (confirm button) -> go to project view

    #if exit/back button pressed, return to main menu

    return

def AddRisks():
    #removeMenu(buttons) - To Remove Main Menu

    #creates input fields
        #Risk Name
        #Risk Status

    #adds risks to project (confirm button)

    #if exit/back button pressed, return to project view

def AddRequirements():
    #removeMenu(buttons) - To Remove Main Menu

    #create input fields
        #Functional Requirements
        #Non-Functional Requirements

    #get input from fields

    #add requirements to project (confirm button) -> return to project view

    #if exit/back button pressed, return to project view

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

    #add week to project (confirm button) -> return to project view

    #if exit/back button pressed, return to main menu

    return

def ViewProject():
    #removeMenu(buttons) - To Remove Main Menu

    #prompts user for project to display
    #display that project's info + risks + requirements

    #if exit/back button pressed, return to main menu

    return

def ViewHours():
    #removeMenu(buttons) - To Remove Main Menu

    #display project hours organized by type

    #if exit/back button pressed, return to project view

    return



#def Writer(i, input):
#    projectwriter = Project()
#    projectwriter.editRow('Project', i, input)
#    return

def StringAdder(Stuff, Stuffinput):
    Stuff.append(Stuffinput)
    return
