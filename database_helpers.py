import sqlite3
from flask import redirect, url_for

def get_question(questionid):
    connection = sqlite3.connect('database/2468')
    cursor = connection.cursor()
    return cursor.execute('SELECT * FROM QuestionFour WHERE id = ?', [questionid]).fetchone()

def get_answers(questionid):
    connection = sqlite3.connect('database/2468')
    cursor = connection.cursor()
    return cursor.execute('SELECT * FROM RespondsTo WHERE id = ?', [questionid]).fetchall()

def deleteAnswer(id, answer_text, user):
    connection = sqlite3.connect('database/2468')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM RespondsTo WHERE id = ? AND answer = ?", [id, answer_text])
    connection.commit()
    connection.close()
    return redirect(url_for('question_view.view_question', questionid=id, user=user))

def get_categories():
    connection = sqlite3.connect('database/2468')
    cursor = connection.cursor()
    categories = cursor.execute("SELECT * FROM Categories").fetchall()
    connection.commit()
    connection.close()
    return categories

def update_question_item(questionid, attribute, value):
    connection = sqlite3.connect('database/2468')
    cursor = connection.cursor()
    cursor.execute("UPDATE QuestionFour SET " + attribute + " = ? WHERE id = ?", [value, questionid])
    connection.commit()
    connection.close()
