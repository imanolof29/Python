from window import *
from connection import *
from tkinter import filedialog
from tkinter import messagebox as message
from tkinter import ttk
from tkinter import * 
import subprocess, os
from tkinter import filedialog

class Viewer(Window):
    def __init__(self, title, size):
        super().__init__(title, size)

        self.app.resizable(0,0)

        self.lbl_text = Label(self.app, text = 'Saved Files')
        self.lbl_text.pack()

        self.btn_delete = Button(self.app, text = 'Delete file', command = self.delete)
        self.btn_delete.place(width = 100, height = 20, x = 150, y = 350)

        self.btn_open = Button(self.app, text ='Open file', command = self.open)
        self.btn_open.place(width = 100, height = 20, x = 150, y = 300)
        
        self.data = None

        #listbox element and how to fill it
        self.lst_list = Listbox(self.app)
        self.fill_list()
        self.lst_list.insert(END, *self.data)
        self.lst_list.place(width = 350, height = 200, x = 25, y = 100)

        self.app.mainloop()

    #when a file is inserted this method is called to load data and fill the listbox
    def fill_list(self):
        c = Db_connection()
        self.data = c.read_files()

    def delete(self):
        #gets the id of the selected file
        id = self.get_id()
        conn = Db_connection()
        if conn.delete_file(id) == True:
            #erases from the list the deleted file
            self.lst_list.delete(ACTIVE)
            message.showinfo(title = 'Success', message = 'The file was deleted successfully')
        else:
            message.showerror(title = 'Error', message = 'There was an error')
    
    def open(self):
        id = self.get_id()
        conn = Db_connection()
        row = conn.get_the_file(id)
        ffile = row[1].decode('utf-8')
        name = row[2]
        extension = row[3]

        path = filedialog.askdirectory()

        f = open(path + '/' + name + extension, 'a+')
        f.write(ffile)
        
       
        
    
    def get_id(self):
        id = int(self.lst_list.get(ACTIVE)[0])
        return id