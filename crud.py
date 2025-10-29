from sqlite3 import *

def init_db():
    with open("schema.sql", encoding="utf-8") as file:
        with connect('data.db') as connection:
            connection.executescript(file.read())
            connection.commit()


def add_student(name, age, major):
    with connect('data.db') as connection:
        cursor = connection.cursor()
        students = cursor.execute('INSERT INTO students (name, age, major) values (?, ?, ?)', [name, age, major])
        connection.commit()
        cursor.close()

def get_all_students():
    with connect('data.db') as connection:
        cursor = connection.cursor()
        students = cursor.execute('SELECT * FROM students').fetchall()
        cursor.close()
    return students