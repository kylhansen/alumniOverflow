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
