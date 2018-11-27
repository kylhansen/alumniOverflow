import sqlite3
import datetime
from flask import Blueprint, render_template, request, redirect, url_for

question_view = Blueprint('question_view', __name__, template_folder='templates')

@question_view.route('/question/<questionid>/<user>', methods=["POST", "GET"])
def view_question(questionid, user):
    connection = sqlite3.connect('database/2468')
    cursor = connection.cursor()
    question = cursor.execute('SELECT * FROM QuestionFour WHERE id = ?', [questionid]).fetchone()
    if not question:
        return "<i>page not found</i>"
    responses = cursor.execute('SELECT * FROM RespondsTo WHERE id = ?', [questionid]).fetchall()
    if user not in ("viewer", "moderator", "expert"):
        return "<i>page not found</i>"
    if request.method=="POST":
        if user == "moderator":
            if "delete" in request.form.keys():
                cursor.execute("DELETE FROM QuestionFour WHERE id = ?", [questionid]) #Delete the question from the database.
                cursor.execute("DELETE FROM RespondsTo WHERE id = ?", [questionid])   #Delete the answers for the question, too.
                connection.commit()
                return redirect(url_for('list_questions.display', user=user))
            question_text = request.form["question_text"]
            category = request.form["category"]
            if category != "":
                all_categories = cursor.execute('SELECT category FROM Categories').fetchall()
                if (category,) not in all_categories: #Verify that the given category actually is a category.
                    return "Invalid Category"
                else:
                    cursor.execute("UPDATE QuestionFour SET category = ? WHERE id = ?", [category, questionid])
            cursor.execute("UPDATE QuestionFour SET (question, published) = (?, ?) WHERE id = ?", [question_text, True, questionid]) #Update question text and publish.
            question = cursor.execute('SELECT * FROM QuestionFour WHERE id = ?', [questionid]).fetchone() #Refresh the question so they can see the changes they made.
            #Do not return here. Continue to serve the template like normal, so the user can see their own edits applied.
        elif user == "expert":
            answer_text = request.form["answer_text"]
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
            email = request.form["email"]
            cursor.execute("DELETE FROM RespondsTo WHERE (responder_email, id) = (?, ?)", [email, questionid]) #If they already answered, replace their old answer with the new one.
            cursor.execute("INSERT INTO RespondsTo VALUES (?,?,?,?)", [email, timestamp, questionid, answer_text]) #Whether or not they already answered, add the new answer to the database.
            connection.commit()
            responses = cursor.execute('SELECT * FROM RespondsTo WHERE id = ?', [questionid]).fetchall() #Refresh responses so they can see the changes they made.
            #Do not return here. Continue to serve the template like normal, so the user can see their own answer added.
        else:
            raise RuntimeError("Unexpected POST for /question/{}/{}".format(questionid, user))
    return render_template('question_view.html', question=question, answers=responses, user=user)
