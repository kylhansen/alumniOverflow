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
            email = request.form["email"]
            update_answer(questionid, email, answer_text)
        else:
            raise RuntimeError("Unexpected POST for /question/{}/{}".format(questionid, user))
    question = get_question(questionid)
    responses = get_answers(questionid)
    if not question:
        return "<i>page not found</i>"
    if user not in ("viewer", "moderator", "expert"):
        return "<i>page not found</i>"
    return render_template('question_view.html', question=question, answers=responses, user=user, back_url=url_for('list_questions.display', user=user))
