from flask import Blueprint, render_template, request, redirect, url_for

question_view = Blueprint('question_view', __name__, template_folder='templates')

@question_view.route('/question/<questionid>/<action>', methods=["POST", "GET"])
def view_question(questionid, action):
    if action not in ("view", "review", "answer"):
        return "Sorry, that doesn't work." #TODO: Handle this better in the future.
    if request.method=="POST":
        #Do POST request things here, once POST functionality exists.
        return ""
    #TODO: Lookup question info by id from the DB, and pass that into the template instead.
    return render_template('question_view.html', questionid=questionid, action=action)
