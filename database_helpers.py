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

def delete_answer(answerid):
    connection = sqlite3.connect('database/2468')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM RespondsTo WHERE answer_id = ?", [answerid])
    connection.commit()
    connection.close()

def delete_question(questionid):
    connection = sqlite3.connect('database/2468')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM QuestionFour WHERE id = ?", [questionid]) #Delete the question from the database.
    cursor.execute("DELETE FROM RespondsTo WHERE id = ?", [questionid])   #Delete the answers for the question, too.
    connection.commit()
    connection.close()

def toggle_published(questionid):
    connection = sqlite3.connect('database/2468')
    cursor = connection.cursor()
    cursor.execute("UPDATE QuestionFour SET published = NOT published WHERE id = ?", [questionid]) #If published, unpublish. If unpublished, publish.
    connection.commit()
    connection.close()

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
