from window import *
from connection import *
from tkinter import filedialog
from tkinter import messagebox as message
from tkinter import * 
from file_viewer import *
from PIL import Image, ImageTk

class App(Window):
    def __init__(self, title, size):
        super().__init__(title, size)
        #makes the window not resizable
        self.app.resizable(0,0)

        self.lbl_text = Label(self.app, text = 'Saved Files')
        self.lbl_text.pack()

        #puts the image on the window
        self.img  = Image.open('lock.png') 
        self.photo=ImageTk.PhotoImage(self.img)
        
        self.lab=Label(image=self.photo)
        self.lab.place(x=75,y=50)
        
        self.btn_browse = Button(self.app, text = 'Browse a file', command = self.browse_file)
        self.btn_browse.place(width = 100, height = 20, x = 150, y = 300)

        self.btn_view = Button(self.app, text = 'View files', command = self.view_files)
        self.btn_view.place(width = 100, height = 20, x = 150, y = 350)

        self.app.mainloop()

    
    def browse_file(self):
        #open file dialog to select your file
        selected = filedialog.askopenfile(initialdir = '/', title = 'Select a file to be saved')
        #converts the file in a blob data to store it 
        blob = self.convert_binary(selected.name)
        #erases the path and gets the file name and extension
        file_name = selected.name.split('/')
        file_name = file_name[len(file_name) - 1]
        #gets the extension of the file
        extension = '.' + file_name.split(".")[1]
        #gets the file's name
        name = file_name.split(".")[0]

        c = Db_connection()
        if c.insert_file(blob, name, extension) == True:
            message.showinfo(title = 'Success', message = 'The file was saved successfully')
        else:
            message.showerror(title = 'Error', message = 'There was an error')

        
    def view_files(self):
        view = Viewer('Explorer', '400x400')

    
    def convert_binary(self, selected):
        with open(selected, 'rb') as file:
            blob = file.read()
        return blob

            
