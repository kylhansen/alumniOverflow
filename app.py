from flask import Flask, render_template, url_for
from survey import survey
from list_questions import list_questions

app = Flask(__name__)
app.secret_key = 'alumniOverflow'
app.url_map.strict_slashes = False

app.register_blueprint(survey)
app.register_blueprint(list_questions)

@app.route('/')
def home():
    return "<a href=" + url_for('survey.survey_q0') + ">Link to survey</a><br><a href="+ url_for('list_questions.display')  + ">Link to view questions</a>" 

if __name__ == '__main__':
    app.run()
