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
mainWindow = tkinter.Tk()
if(first):
    App = AppWindow(master = mainWindow)
    App.editTitle('Project Tracker')
    first = False

App.mainloop()

