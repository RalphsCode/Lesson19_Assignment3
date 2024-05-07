from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
import surveys

app = Flask(__name__)

app.config['SECRET_KEY'] = "Ralph_01234"
debug = DebugToolbarExtension(app)

responses = []

@app.route('/home')
def home():
	satisfaction_survey = surveys.satisfaction_survey
	return render_template('home.html', satisfaction_survey = satisfaction_survey)
