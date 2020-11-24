import tkinter
import gui_util
from gui_util import AppWindow
from tkinter import Tk
#For some reason, JUST importing this module makes the maximize function in Tkinter use the correct screen resolution.
import pyautogui

#This will act as the main for the program.

#To my understanding, this line as well as mainloop(At the end of main) bookend the program main.
#The information between these two will be run in a loop.
mainWindow = tkinter.Tk()

#This initializes the GUI_Utilities class, most functions that interact with tkinter should be clustered in there as functions.
App = AppWindow(master=mainWindow)
App.editTitle('Project Tracker')

#Here's an example of how to put in things into the window.
BackgroundImage = App.enterImage(mainWindow, 'Temp Button-1.png', 'top', App.width, App.height)

App.mainloop()