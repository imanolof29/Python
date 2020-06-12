import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('discord_bot.db')
        self.cursor = self.connection.cursor()

    def insertar(self, frase):
        try:
            self.cursor.execute('INSERT INTO Frases (frase) VALUES (?)', (frase,))
            self.connection.commit()
            return True
        except:
            return False
    
    def borrar(self, id):
        try:
            self.cursor.execute('DELETE FROM Frases WHERE id=?', (id,))
            self.connection.commit()
            return True
        except:
            return False
    
    def leer_frases(self):
        self.cursor.execute('SELECT * FROM Frases')
        data = self.cursor.fetchall()
        return data
