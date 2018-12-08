import sqlite3
import datetime
from database_helpers import *
from flask import Blueprint, render_template, request, redirect, url_for

question_view = Blueprint('question_view', __name__, template_folder='templates')

@question_view.route('/question/<questionid>/<user>', methods=["POST", "GET"])
def view_question(questionid, user):
    if request.method=="POST":
        if user == "moderator":
            if "delete_question" in request.form.keys():
                delete_question(questionid)
                return redirect(url_for('list_questions.display', user=user))
            if "publish_question" in request.form.keys() or "unpublish_question" in request.form.keys():
                toggle_published(questionid)
            if "edit_question" in request.form.keys():
                return redirect(url_for("edit.edit_question", questionid=questionid))
            if "delete_answer" in request.form.keys():
                answerid = int(request.form["which_answer"])
                delete_answer(answerid)
        elif user == "expert":
            answer_text = request.form["answer_text"]
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
            email = request.form["email"]
            cursor.execute("DELETE FROM RespondsTo WHERE (responder_email, id) = (?, ?)", [email, questionid]) #If they already answered, replace their old answer with the new one.
            cursor.execute("INSERT INTO RespondsTo (responder_email, date_responded, id, answer) VALUES (?,?,?,?)", [email, timestamp, questionid, answer_text]) #Whether or not they already answered, add the new answer to the database.
            connection.commit()
            connection.close()
        else:
            raise RuntimeError("Unexpected POST for /question/{}/{}".format(questionid, user))
    question = get_question(questionid)
    responses = get_answers(questionid)
    if not question:
        return "<i>page not found</i>"
    if user not in ("viewer", "moderator", "expert"):
        return "<i>page not found</i>"
    return render_template('question_view.html', question=question, answers=responses, user=user, back_url=url_for('list_questions.display', user=user))
