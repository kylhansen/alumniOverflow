#coding: utf8
#
# Serves a page that laets a client answer the initial survey
#

from flask import Blueprint, session, render_template, request, redirect, url_for
import sqlite3
import os

# There ought to be a global "DB_NAME" and "DB_CONNECT" variables.
file_path = os.path.dirname(os.path.realpath(__file__))
DB_NAME = file_path + '/database/2468'
# We ought to have either fixed categories, or a global database-accessing function which retrieves all categories for us
FIXED_CATEGORIES = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5', 'Category 6', 'Category 7', 'Category 8']

list_questions = Blueprint('list_questions', __name__, template_folder='templates')

# Helper function for setting the user to appropriate strings
def set_user(user):
    if (user=='moderator' or user=='expert'):
        return user
    else:
        return 'viewer'


@list_questions.route('/list_questions/', defaults={'user':None})
@list_questions.route('/list_questions/<user>/')
def display(user):
    user = set_user(user)
    greeting = "Welcome, " + user + "!"
    conn = sqlite3.connect(DB_NAME) #This needs to not be global, otherwise threading errors will happen.
    curs = conn.cursor()
    question_categories = dict()

    # HOPEFULLY these following lines of code will produce a dictionary similar to that in 'test_q_c' as below.
    #   the dictionary should look like: { <category> : <list-of-tuples [ <question>, <question_link> ]> }
    for row in curs.execute('SELECT * FROM QuestionFour'):
        email = row[0]
        category = row[1]
        question = row[2]
        link = url_for('list_questions.question_view') + user
        #published = row[3]
        #link = row[4]
        values = [question, link]
        try:
            question_categories[category].append(values)
        except:
            question_categories[category] = list()
            question_categories[category].append(values)

    link = url_for('list_questions.question_view') + user
    #test_q_c = {'category 1' : [['This is a question about category 1',link], ['This is another question about category 1!', link]], 'this is category 2': [['This is a question about category 2', link], ['I have another question!!!', link], ['this is not a question.', link]]}
    return render_template('list_questions.html',user=user, question_categories=question_categories, greeting=greeting)

# a standin for the "question" view which will be provided by the other team
@list_questions.route('/temp/', defaults={'user':None})
@list_questions.route('/temp/<user>/')
def question_view(user):
    user = set_user(user)
    return render_template('temp.html', user=user)
