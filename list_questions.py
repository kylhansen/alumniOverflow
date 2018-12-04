#coding: utf8
#
# Serves a page that laets a client answer the initial survey
#

from flask import Blueprint, session, render_template, request, redirect, url_for
import sqlite3
import os
from question_view import question_view

# There ought to be a global "DB_NAME" and "DB_CONNECT" variables.
file_path = os.path.dirname(os.path.realpath(__file__))
DB_NAME = file_path + '/database/2468'
# We ought to have either fixed categories, or a global database-accessing function which retrieves all categories for us
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

    conn = sqlite3.connect(DB_NAME)
    curs1 = conn.cursor()

    question_categories = dict()
   
    categories = list()
    for category in curs1.execute('SELECT category FROM Categories;'):
        curs2 = conn.cursor()
        if user != 'moderator':
            published = 'AND published="true"'
        else:
            published = ''
        for row in curs2.execute('SELECT email, category, question, id, published FROM QuestionFour WHERE category = ?' + published + ';', category):
            # The following produces a dictionary of the form below. 
            #   { <category> : <list-of-tuples [ <question>, <question_link> ]> }
            email = row[0]
            category = row[1]
            question = row[2]
            qid = row[3]
            published = row[4]
            
            link = url_for('question_view.view_question', questionid=qid, user=user)
            values = [question, link]

            # Add question/link to dictionary 
            try:
                question_categories[category].append(values)
            except:
                question_categories[category] = list()
                question_categories[category].append(values)

    #test_q_c = {'category 1' : [['This is a question about category 1',link], ['This is another question about category 1!', link]], 'this is category 2': [['This is a question about category 2', link], ['I have another question!!!', link], ['this is not a question.', link]]}
    return render_template('list_questions.html',user=user, question_categories=question_categories, greeting=greeting)
