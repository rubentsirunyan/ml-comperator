import sqlite3

from Comperator import app

db = '/home/rtsirunyan/Documents/Projects/Comperator/db/demo.db' 
# db = app.config['DATABASE']
class TrainingData():
    
    def __init__(self):
        self.conn = sqlite3.connect(db)
        self.conn.row_factory = sqlite3.Row
        self.conn.text_factory = str

    def get_all(self):
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM data")
        return self.c.fetchall()

    def get_pretty(self):
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM data LIMIT 20")
        self.rows = self.c.fetchall()
        self.temp_list = []
        for row in self.rows:
            self.columns = row.keys()
            self.temp_row = []
            for i, elem in enumerate(row):
                if "L0" in self.columns[i]:
                    self.c.execute("SELECT Value FROM L0 WHERE Id={}".format(elem))
                    self.temp_row.append(self.c.fetchone()[0])
                elif "L1" in self.columns[i]:
                    self.c.execute("SELECT Value FROM L1 WHERE Id={}".format(elem))
                    self.temp_row.append(self.c.fetchone()[0])
                elif "L2" in self.columns[i]:
                    self.c.execute("SELECT Value FROM L2 WHERE Id={}".format(elem))
                    self.temp_row.append(self.c.fetchone()[0])
                elif "L3" in self.columns[i]:
                    self.c.execute("SELECT Value FROM L3 WHERE Id={}".format(elem))
                    self.temp_row.append(self.c.fetchone()[0])
                elif "L4" in self.columns[i]:
                    self.c.execute("SELECT Value FROM L4 WHERE Id={}".format(elem))
                    self.temp_row.append(self.c.fetchone()[0])
                else:
                    self.temp_row.append(str(elem))
            self.temp_list.append(self.temp_row)
        return self.columns, self.temp_list

    def __repr__(self):
        return '<Data %r>' % (self.get_all()[0])