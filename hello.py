from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/resume')
@app.route('/cv')
def resume():
    return render_template('resume.html')
