from window import *
from connection import *
from app import *

class First(Window):
    def __init__(self, title, size):
        super().__init__(title, size)
        self.PASSWORD = '123'

        self.text = Label(self.app, text = 'Type your password')
        self.text.pack()

        self.password = Entry(self.app, show = '*')
        self.password.pack()

        self.submit = Button(self.app, text = 'Submit', command = self.check_password)
        self.submit.pack()

        self.app.mainloop()

    def check_password(self):
        if self.password.get() == self.PASSWORD:
            self.app.destroy()
            a = App('Main Menu', '400x400')


if __name__ == '__main__':
    f = First('Password', '300x300')
    
        