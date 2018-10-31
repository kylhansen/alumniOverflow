from flask import Blueprint, session, render_template, request, redirect, url_for

search = Blueprint('survey', __name__, template_folder='templates')

@search.route('/search/<user>/', methods=["POST", "GET"])
def search(user):
    if user == 'moderator':
        greeting = 'Welcome, moderator!'
    elif user == 'expert':
        greeting = 'Welcome, expert!'
    else
        greeting = 'Welcome!'
    return('answer.html', greeting=greeting, question_view='temp.html')

