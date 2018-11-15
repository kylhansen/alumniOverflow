import sqlite3
import datetime
from flask import Blueprint, render_template, request, redirect, url_for

question_view = Blueprint('question_view', __name__, template_folder='templates')

@question_view.route('/question/<questionid>/<action>', methods=["POST", "GET"])
def view_question(questionid, action):
    connection = sqlite3.connect('database/2468')
    cursor = connection.cursor()
    question = cursor.execute('SELECT * FROM QuestionFour WHERE id = {}'.format(questionid)).fetchone()
    responses = cursor.execute('SELECT * FROM RespondsTo WHERE id = {}'.format(questionid)).fetchall()
    if action not in ("view", "review", "answer"):
        return "<i>page not found</i>"
    if request.method=="POST":
        if action == "review":
            question_text = request.form["question_text"]
            category = request.form["category"]
            published = request.form["published"]
            delete = request.form["delete"]
            return "TODO: Redirect back to questions list."
        elif action == "answer":
            answer_text = request.form["answer_text"] #May be the text of a new answer or alternately the revision of an existing answer paired with the given email addres. Which one is asked for is handled by javascript.
            timestamp = datetime.datetime.now().strftime("%m/%d/%Y")
            email = request.form["email"]
            #Does not return anything, because we in fact want to redirect the answerer back to the question itself so they can see their answer.
        else:
            raise RuntimeError("Unexpected POST for /question/{}/{}".format(questionid, action))
    return render_template('question_view.html', question=question, answers=responses, action=action)
