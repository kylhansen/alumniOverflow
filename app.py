from flask import Flask
from alumniOverflow.survey_q4 import survey_q4
app = Flask(__name__)


app.register_blueprint(survey_q4)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
