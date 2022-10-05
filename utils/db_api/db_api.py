import sqlite3


def connect():
    global cur, con
    con = sqlite3.connect("../../data/DataBase/quiz.db")
    cur = sqlite3.Cursor()

def add_some_info():
    pass