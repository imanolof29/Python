from tkinter import *
from tkinter import messagebox as mensaje
#para usar el conector de mysql hay que instalarlo primero
#pip install mysql-connector
import mysql.connector

class Ventana:
    def __init__(self):
        self.root = Tk()
        self.root.title("Login")
        self.root.geometry("300x300")
        self.elementos()
        self.root.mainloop()

    
    def elementos(self):
        #Etiqueta correo
        self.lbl_correo = Label(self.root, text = "Correo")
        self.lbl_correo.pack()
        
        #Entrada de texto para el correo
        self.txt_correo = Entry(self.root)
        self.txt_correo.pack()

        #Etiqueta contraseña
        self.lbl_contrasena = Label(self.root, text = "Contraseña")
        self.lbl_contrasena.pack()

        #Entrada de texto para la contraseña
        self.txt_contrasena = Entry(self.root,  show = '*')
        self.txt_contrasena.pack()

        #Boton aceptar con la funcion enviar al hacer click
        self.aceptar = Button(text = "Aceptar", command = self.enviar)
        self.aceptar.pack()
    
    
    def enviar(self):
        #Validacion de campos
        if self.txt_correo.get() == "" or self.txt_contrasena.get() == "":
            mensaje.showwarning(title = "Error", message = "Rellene los campos vacios")
        else:
            try:
                #Establecer la conexion con la BBDD
                db = mysql.connector.connect(host = '', database ='', user = '', password = '')
                cursor = db.cursor()
                cursor.execute('SELECT * FROM usuarios WHERE correo = %s AND contrasena = %s', (self.txt_correo.get(), self.txt_contrasena.get()))
                if cursor.fetchall():
                    mensaje.showinfo(title = "Login", message = "Bienvenido")
                else:
                    mensaje.showerror(title = "Login", message = "Usuario o contraseña incorrecta")

                cursor.close()
            except:
                mensaje.showwarning(title = "Error", message = "Hubo algun problema con la conexion a la base de datos")
            
    


if __name__ == "__main__":
    v = Ventana()