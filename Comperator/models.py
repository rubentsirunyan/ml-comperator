import sqlite3
import csv
from Comperator import app
import numpy as np
import json

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
        self.rows = self.c.fetchall()
        self.columns =  self.rows[0].keys()
        return self.columns, self.rows
    

    def get_pretty(self, limit):
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM data LIMIT {}".format(limit))
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

class DataCSV():

    def get_train_pretty(self):
        self.columns = []
        self.data = []       
        with open('db/columns.txt', 'r') as f:
            for line in f:
                self.columns.append(line)
        with open('db/training_data.csv', 'r') as f:
            with open('db/dict.json', 'r') as d:
                self.dict = json.load(d)
                self.csv_reader = csv.reader(f,
                                    delimiter=',',
                                    quotechar='|',
                                    quoting=csv.QUOTE_NONNUMERIC)
                for line in self.csv_reader:
                    self.temp_row = []
                    for i, elem in enumerate(line):
                        if "L0" in self.columns[i]:
                            self.temp_row.append(self.dict["L0"]["{}".format(int(elem))])
                        elif "L1" in self.columns[i]:
                            self.temp_row.append(self.dict["L1"]["{}".format(int(elem))])
                        elif "L2" in self.columns[i]:
                            self.temp_row.append(self.dict["L2"]["{}".format(int(elem))])
                        elif "L3" in self.columns[i]:
                            self.temp_row.append(self.dict["L3"]["{}".format(int(elem))])
                        elif "L4" in self.columns[i]:
                            self.temp_row.append(self.dict["L4"]["{}".format(int(elem))])
                        else:
                            self.temp_row.append(str(elem))
                    self.data.append(self.temp_row)
        return self.columns, self.data   
        
    def get_test_pretty(self):
        self.columns = []
        self.data = []       
        with open('db/columns.txt', 'r') as f:
            for line in f:
                self.columns.append(line)
        with open('db/eval_data.csv', 'r') as f:
            with open('db/dict.json', 'r') as d:
                self.dict = json.load(d)
                self.csv_reader = csv.reader(f,
                                    delimiter=',',
                                    quotechar='|',
                                    quoting=csv.QUOTE_NONNUMERIC)
                for line in self.csv_reader:
                    self.temp_row = []
                    for i, elem in enumerate(line):
                        if "L0" in self.columns[i]:
                            self.temp_row.append(self.dict["L0"]["{}".format(int(elem))])
                        elif "L1" in self.columns[i]:
                            self.temp_row.append(self.dict["L1"]["{}".format(int(elem))])
                        elif "L2" in self.columns[i]:
                            self.temp_row.append(self.dict["L2"]["{}".format(int(elem))])
                        elif "L3" in self.columns[i]:
                            self.temp_row.append(self.dict["L3"]["{}".format(int(elem))])
                        elif "L4" in self.columns[i]:
                            self.temp_row.append(self.dict["L4"]["{}".format(int(elem))])
                        else:
                            self.temp_row.append(str(elem))
                    self.data.append(self.temp_row)
                    
        return self.columns, self.data   


    def train_data(self):
        self.features = []
        self.labels = []
        with open('db/training_data.csv', 'r') as f:
            self.csv_reader = csv.reader(f,
                                delimiter=',',
                                quotechar='|',
                                quoting=csv.QUOTE_NONNUMERIC)
            for line in self.csv_reader:
                self.features.append(line[:-1])
                self.labels.append(line[-1])
        return np.array(self.features), np.array(self.labels)
    
    def train_data_personal(self):
        self.features = []
        self.labels = []
        with open('db/training_data.csv', 'r') as f:
            self.csv_reader = csv.reader(f,
                                delimiter=',',
                                quotechar='|',
                                quoting=csv.QUOTE_NONNUMERIC)
            for line in self.csv_reader:
                self.features.append(line[43:-1])
                self.labels.append(line[-1])
        return np.array(self.features), np.array(self.labels)

    def train_data_supersampled(self):
        self.features = []
        self.labels = []
        with open('db/training_data.csv', 'r') as f:
            self.csv_reader = csv.reader(f,
                                delimiter=',',
                                quotechar='|',
                                quoting=csv.QUOTE_NONNUMERIC)
            for line in self.csv_reader:
                if line[-1] == 1.0:
                    for _ in range(15):
                        self.features.append(line[:-1])
                        self.labels.append(line[-1])
                else:
                    self.features.append(line[:-1])
                    self.labels.append(line[-1])
        return np.array(self.features), np.array(self.labels)


    def eval_data(self):
        self.predictions = []
        with open("db/eval_data.csv",'r') as f:
            self.csv_reader = csv.reader(f, 
                                delimiter=',',
                                quotechar='|',
                                quoting=csv.QUOTE_NONNUMERIC)
            for line in self.csv_reader:
                self.predictions.append(line)
        return np.array(self.predictions)
    def eval_data_personal(self):
        self.predictions = []
        with open("db/eval_data.csv",'r') as f:
            self.csv_reader = csv.reader(f, 
                                delimiter=',',
                                quotechar='|',
                                quoting=csv.QUOTE_NONNUMERIC)
            for line in self.csv_reader:
                self.predictions.append(line[43:])
        return np.array(self.predictions)


    def target_data(self):
        self.targets = []
        with open("db/targets.txt",'r') as f:  
            for line in f:
                self.targets.append(float(line))
        return self.targets