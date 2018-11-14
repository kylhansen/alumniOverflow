#coding: utf8
# 
# Serves a page that laets a client answer the initial survey 
# 

import sqlite3
from flask import Blueprint, session, render_template, request, redirect, url_for

survey = Blueprint('survey', __name__, template_folder='templates')

@survey.route('/survey_q0', methods=["POST", "GET"])
def survey_q0():
    # Collect responses on personal information
    if request.method=="POST":
        # TODO: if needed, put in database here. 
        #   Otherwise, wait to add all data at the end, and save all this in the session (Probably the latter)
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        email = request.form['email']
        dob = request.form['dob']
        institution = request.form['institution']
        grad_year = request.form['graddate']
        majors = request.form['majors']

        # Add all keys to the session with the user input data 
        session['first_name'] = first_name
        session['last_name'] = last_name
        session['email'] = email
        session['dob'] = dob
        session['institution'] = institution
        session['grad_year'] = grad_year
        session['majors'] = majors

        
        return redirect(url_for('survey.survey_q1'))

    # Render demographic/personal information question
    return render_template('survey_q0.html')

@survey.route('/survey_q1', methods=["POST", "GET"])
def survey_q1():
    # Read in the categories present in the database
    categories = get_categories()

    # Process submission and send user to next page
    if request.method=="POST":
        # Fetch the categories which the user selected and put them in a list
        selected_categories = list()
        for key in request.form.keys():
            if request.form[key]:
                selected_categories.append(key)
        # Save all categories selected
        session['categories'] = selected_categories

        # Send the user to the next question
        return redirect(url_for('survey.survey_q2'))

    # Render question 1
    return render_template('survey_q1.html', categories = categories)

@survey.route('/survey_q2', methods=["POST", "GET"])
def survey_q2():
    if request.method=="POST":
        categories = list()
        # Fetch the categories which were selected and put them in a list
        for value in request.form.values():
            categories.append(value)

        # Save top categories selected
        session['top_categories'] = categories

        # Send the user to the next question
        return redirect(url_for('survey.survey_q3'))

    # Render question 2
    return render_template('survey_q2.html', selected_categories=session['categories'])    

@survey.route('/survey_q3', methods=["POST", "GET"])
def survey_q3():
    if request.method == "POST":
        # Fetch the categories which the user selected and put them in a list
        categories = list()
        for key in request.form.keys():
            if request.form[key]:
                categories.append(key)

        # Save categories for which they don't know everything they need
        session['question_categories'] = categories

        # Send the user to the next question
        return redirect(url_for('survey.survey_q4'))

    # Render question 3
    return render_template('survey_q3.html', top_categories=session['top_categories'])

@survey.route('/survey_q4', methods=["POST", "GET"])
def survey_q4():
    if request.method=="POST":
        c_and_q = dict()
        # Fetch the category/question pair for the response
        for category,question in request.form.items():
            c_and_q[category] = question
        # TODO: pass all relevant information from the session off to the database
        session['c_and_q'] = c_and_q
        
        #loads all data into database
        load_db()

        # Send the user to the "thank you" page
        return render_template("survey_end.html")
    
    # Render question 4
    return render_template("survey_q4.html", question_categories=session['question_categories'])


def get_categories():
    conn = sqlite3.connect('database/2468')
    c = conn.cursor()

    categories = set()
    for row in c.execute('SELECT category FROM categories'):
        categories.add(row[0])
        
    c.close()
    conn.close()
    return categories


def load_db():
    #opens connection with the local database, and creates a cursor that allows commands to be sent to the database
    conn = sqlite3.connect('database/2468')
    c = conn.cursor()
   

    #list of data to be inserted into participants table
    insert_list_par = [(str(session['first_name']), str(session['last_name']), str(session['email']),
                         str(session['dob']), str(session['institution']), str(session['grad_year']),
                         str(session['majors']))]
        
    #saves command that inserts user input into the Participants table of the local database to be excuted later at end of function call
    c.executemany('INSERT INTO Participants VALUES (?,?,?,?,?,?,?)', insert_list_par)
    
    
    #inserts data into question one table
    for cat in session['categories']:
       insert_list_q1 = [session['email'], cat] 
       c.execute('INSERT INTO QuestionOne VALUES (?,?)', insert_list_q1)
       insert_list_q1 = list()
       
    #inserts data into question two table
    for cat in session['top_categories']:
       insert_list_q2 = [session['email'], cat] 
       c.execute('INSERT INTO QuestionTwo VALUES (?,?)', insert_list_q2)
       insert_list_q2 = list()
       
    #inserts data into question three table
    for cat in session['question_categories']:
       insert_list_q3 = [session['email'], cat] 
       c.execute('INSERT INTO QuestionThree VALUES (?,?)', insert_list_q3)
       insert_list_q3 = list()
       

    #inserts data into question 4 table
    insert_list_q4 = []
    c_and_q = session['c_and_q']
    for category in c_and_q:
        insert_list_q4.append((session['email'],category,c_and_q[category],"False"))

    c.executemany('INSERT INTO QuestionFour (email,category,question,published) VALUES (?,?,?,?)', insert_list_q4)

    #sends all commands in one swell foop so it is atomic, and closes local database connection
    conn.commit()
    c.close()
    conn.close()









