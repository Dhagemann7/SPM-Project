import tkinter
import gui_util
from gui_util import AppWindow
from tkinter import *
#This will act as the main for the program.

#To my understanding, this line as well as mainloop(At the end of main) bookend the program main.
#The information between these two will be run in a loop.
mainWindow = tkinter.Tk()

#This initializes the GUI_Utilities class, most functions that interact with tkinter should be clustered in there as functions.
App = AppWindow(master=mainWindow)

App.mainloop()