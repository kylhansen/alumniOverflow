import sqlite3
import datetime
from database_helpers import *
from flask import Blueprint, render_template, request, redirect, url_for

edit = Blueprint('edit', __name__, template_folder='templates')

# handle edits to a question text or category for a question with the given id
@edit.route('/question/<questionid>/moderator/edit', methods=["POST", "GET"])
def edit_question(questionid):

    # get the question tuple from the database for the given id
    question = get_question(questionid)
    old_category = question[2]
    old_text = question[3]
    
    # run if the moderator clicks 'cancel' or 'save'
    if request.method=="POST":
    
        # if the moderator saves changes, save into database
        if "save" in request.form.keys():
            connection = sqlite3.connect('database/2468')
            cursor = connection.cursor()
            new_text = request.form['question_text']
            new_category = request.form['category']
            update_question_item(questionid, "category", new_category)
            update_question_item(questionid, "question", new_text)

        # return to the question view page
        return redirect(url_for('question_view.view_question', questionid=questionid, user="moderator"))

    #render the template for the edit page (currently just a temp file)
    categories = get_categories()
    return render_template('temp.html', old_category=old_category, old_text=old_text, categories=categories)

