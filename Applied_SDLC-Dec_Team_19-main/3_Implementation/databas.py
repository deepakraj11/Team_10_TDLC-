import sqlite3 as sl
import os
from src import workoutplan as w
 
# THIS FUNCTION CAN BE CALLED DURING INITIAL CONFIG
def create():
 
    os.remove("test_db")
    con=sl.connect('test_db')
 
    with con:
        con.execute("""
            CREATE TABLE USER (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                gender TEXT,
                weight INTEGER,
                Height INTEGER,
                Activity TEXT,
                Goal TEXT
            );
        """)
    
 
# THIS FUNCTION CAN BE CALLED TO UPDATE DATA
def insert(height, weight):
    con=sl.connect('test_db')
 
    '''
 
    USER INPUT CAN BE TAKEN HERE
 
    '''
 
    with con:
        sql = 'INSERT OR REPLACE INTO USER (id, name, age, weight, Height) values(?, ?, ?, ?, ?)'
    data = [
        (0 , " ", " ", weight, height)
    ]
 
    with con:
        con.executemany(sql, data)
 
    with con:
       data = con.execute("SELECT* FROM USER WHERE age <= 24")
 
       for row in data:
           print(row)
def fetchheight():
    con=sl.connect('test_db')
 
    cursor = con.cursor()
 
    sqlite_select_query = """SELECT Height from USER"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
 
    for row in records:
        Height=row[0]
    return Height
def fetchweight():
    con=sl.connect('test_db')
 
    cursor = con.cursor()
 
    sqlite_select_query = """SELECT weight from USER"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
 
    for row in records:
        weight=row[0]
    return(weight)

create()