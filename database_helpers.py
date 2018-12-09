import sqlite3
import datetime
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

def update_answer(questionid, email, answer_text):
    connection = sqlite3.connect('database/2468')
    cursor = connection.cursor()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
    cursor.execute("DELETE FROM RespondsTo WHERE (responder_email, id) = (?, ?)", [email, questionid]) #If they already answered, replace their old answer with the new one.
    cursor.execute("INSERT INTO RespondsTo (responder_email, date_responded, id, answer) VALUES (?,?,?,?)", [email, timestamp, questionid, answer_text]) #Whether or not they already answered, add the new answer to the database.
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
