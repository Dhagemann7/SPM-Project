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

#frame1 = App.createFrame(parent=App, side = "top", h = 300, w = 300, bg = "red")
frame5 = Frame(mainWindow, bg = "red", height = 300, width = 300)
frame5.pack(side = tkinter.TOP)
frame4 = Frame(frame5, bg = "yellow", height = 30, width = 30)
frame4.pack(side = tkinter.LEFT)
#frame2 = App.createFrame(parent=frame1, side="left", h = 30, w = 30, bg = "yellow")
#frame3 = App.createFrame(parent=frame1, side="right", h = 30, w = 30, bg = "yellow")

App.mainloop()