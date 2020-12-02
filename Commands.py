import os
import tkinter
import sys
from tkinter import *
import ProjectUtil
from ProjectUtil import Project

def ExitButton():
    sys.exit()
    return

def AddProject(name,owner,members,description,risks,riskStatus):
    newProj = Project()
    newProj.createFile(name, owner, members, description, risks, riskStatus)
    #App.removeprojectmenu()
    #create new Project object from inputs (confirm button) -> go to project view
        #Project Name
        #Project Owner
        #Project Team Members
        #Project Description

    #newProject = Project(name,owner,members,description)

    #add Project object to array of projects

    #go to project view

    return

def AddRisks(project,riskName,status):
    #adds risks to existing project (confirm button)
        #Risk Name
        #Risk Status

    #project.addRisk(riskName,status)

    #return to project view

    return

def AddRequirements(project, rtype, requirement):
    #add requirements to project (confirm button)
        #Functional Requirements
        #Non-Functional Requirements

    #project.addRequirement(rtype, requirement)

    # return to project view

    return

def AddHours(project,week,requirementsHours,designHours,codingHours,testingHours,projManagementHours):
    #add hours to project (confirm button)
        #Week Number
        #Requirements Analysis Hours
        #Design Hours
        #Coding Hours
        #Testing Hours
        #Project Management Hours

    #project.addWeekHours(requirementsHours,designHours,codingHours,testingHours,projManagementHours)

    #return to project view

    return

#def Writer(i, input):
#    projectwriter = Project()
#    projectwriter.editRow('Project', i, input)
#    return

def StringAdder(Stuff, Stuffinput):
    Stuff.append(Stuffinput)
    return

def sequence(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func