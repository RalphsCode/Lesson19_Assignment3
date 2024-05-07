from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
import surveys

# Globally scoped variables
responses = []
survey = {}

app = Flask(__name__)

app.config['SECRET_KEY'] = "Ralph_01234"
debug = DebugToolbarExtension(app)

@app.route('/home')
def home():
	global survey 
	survey = surveys.satisfaction_survey
	return render_template('home.html', survey = survey)

@app.route('/questions/<int:number>', methods=['GET', 'POST'])
def questions(number):
	global survey
	if number <= len(survey.questions):
		if number >=2:
			print('setting session')
			responses.append(request.form.get('answer', 'None'))
			session['answers'] = responses
		return render_template('questions.html', survey=survey, number=number)
	else:
		responses.append(request.form.get('answer', 'None'))
		session['answers'] = responses
		return render_template('thanks.html')
  