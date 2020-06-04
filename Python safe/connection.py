import sqlite3

class Db_connection:

    def __init__(self):
        self.connection = sqlite3.connect('dbase.db')
        self.cursor = self.connection.cursor()
    

    def insert_file(self, blob, name, extension):
        try:
            self.cursor.execute('INSERT INTO Files (file, name, extension) VALUES (?, ?, ?)', (blob, name, extension))
            self.connection.commit()
            self.cursor.close()
            return True
        except:
            return False

    def read_files(self):
        data = None
        self.cursor.execute('SELECT id, name, extension FROM Files')
        data = self.cursor.fetchall()
        self.cursor.close()
        return data

    def delete_file(self, id):
        try:
            self.cursor.execute('DELETE FROM Files WHERE id=?', (id,))
            self.connection.commit()
            self.cursor.close()
            return True
        except:
            return False
    
    def get_the_file(self, id):
        self.cursor.execute('SELECT * FROM Files WHERE id=?', (id,))
        row =  self.cursor.fetchone()
        self.cursor.close()
        return row




        

