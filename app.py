from flask import Flask
#from alumniOverflow.survey_q4 import survey_q4
from survey import survey

app = Flask(__name__)
app.secret_key = 'alumniOverflow'

#app.register_blueprint(survey_q4)
app.register_blueprint(survey)
app.register_blueprint(search)

@app.route('/')
def home():
    return ("<a href='{{ survey }}'>Link to survey</a>", survey=url_for(survey.survey_q0))

if __name__ == '__main__':
    app.run()
