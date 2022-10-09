import sqlite3


def connect(db_name):
    con = sqlite3.connect(f"../../data/DataBase/{db_name}.db")
    cur = sqlite3.Cursor(con)
    return con, cur


def get_some_info(db_name, get_what, get_from):
    connection, cursor = connect(db_name)
    connection.execute(f"SELECT {get_what} FROM {get_from}")
    print(cursor.fetchall())


def add_some_info(db_name, add_what, add_where):
    connection, cursor = connect(db_name)
    connection.execute(f"INSERT INTO {add_where} VALUES({add_what})")


add_some_info("users_logs", "UserName", "users")

get_some_info("users_logs", "*", "users")