import sqlite3

def get_question(questionid):
    connection = sqlite3.connect('database/2468')
    cursor = connection.cursor()
    return cursor.execute('SELECT * FROM QuestionFour WHERE id = ?', [questionid]).fetchone()

def get_answers(questionid):
    connection = sqlite3.connect('database/2468')
    cursor = connection.cursor()
    return cursor.execute('SELECT * FROM RespondsTo WHERE id = ?', [questionid]).fetchall()
