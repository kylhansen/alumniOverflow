from flask import Flask
#from alumniOverflow.survey_q4 import survey_q4
from survey import survey

app = Flask(__name__)
app.secret_key = 'alumniOverflow'

#app.register_blueprint(survey_q4)
app.register_blueprint(survey)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
