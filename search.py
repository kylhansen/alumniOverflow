#coding: utf8
# 
# Serves a page that laets a client answer the initial survey 
# 

from flask import Blueprint, session, render_template, request, redirect, url_for

search = Blueprint('search', __name__, template_folder='templates')

@search.route('/search', defaults={'user':None})
@search.route('/search/<user>/')
def search_questions(user):
    if user == 'moderator':
        greeting = 'Welcome, moderator!'
    elif user == 'expert':
        greeting = 'Welcome, expert!'
    else:
        greeting = 'Welcome!'
    return render_template('answer.html', greeting=greeting, question_view=url_for('search.question_view'))

# a standin for the "question" view which will be provided by the other team
@search.route('/temp')
def question_view():
    return render_template('temp.html')

