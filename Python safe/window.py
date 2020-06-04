from tkinter import *

class Window:
    def __init__(self, title, size):
        self.title = title
        self.size = size
        self.app = Tk()
        self.app.geometry(self.size)
        self.app.title(self.title)

        #the mainloop goes on the child class



    