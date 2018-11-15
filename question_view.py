import sqlite3
import datetime
from flask import Blueprint, render_template, request, redirect, url_for

question_view = Blueprint('question_view', __name__, template_folder='templates')

@question_view.route('/question/<questionid>/<user>', methods=["POST", "GET"])
def view_question(questionid, user):
    connection = sqlite3.connect('database/2468')
    cursor = connection.cursor()
    question = cursor.execute('SELECT * FROM QuestionFour WHERE id = {}'.format(questionid)).fetchone()
    responses = cursor.execute('SELECT * FROM RespondsTo WHERE id = {}'.format(questionid)).fetchall()
    if user not in ("viewer", "moderator", "expert"):
        return "<i>page not found</i>"
    if request.method=="POST":
        if user == "moderator":
            question_text = request.form["question_text"]
            category = request.form["category"]
            published = request.form["published"]
            delete = request.form["delete"]
            return "TODO: Redirect back to questions list."
        elif user == "expert":
            answer_text = request.form["answer_text"] #May be the text of a new answer or alternately the revision of an existing answer paired with the given email addres. Which one is asked for is handled by javascript.
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
            email = request.form["email"]
            cursor.execute("INSERT INTO RespondsTo VALUES (?,?,?,?)", [email, timestamp, questionid, answer_text])
            connection.commit()
            responses = cursor.execute('SELECT * FROM RespondsTo WHERE id = {}'.format(questionid)).fetchall() #Refresh responses.
            #Continue to serve the template like normal, so the user can see their own answer added.
        else:
            raise RuntimeError("Unexpected POST for /question/{}/{}".format(questionid, user))
    return render_template('question_view.html', question=question, answers=responses, user=user)
