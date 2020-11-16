from tkinter import *

class GUI_Utilities:
    def __init__(self):
        self.root = Tk()
        self.root.title("Title")
        self.root.mainloop()
        self.screenheight = self.root.winfo_screenheight()
        self.screenwidth = self.root.winfo_screenwidth()
