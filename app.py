from flask import Flask, request, render_template, redirect, flash, session, url_for
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
	return render_template('home.html', survey = survey)

@app.route('/questions/<int:number>', methods=['GET', 'POST'])
def questions(number):
	global survey
	# Check if there are any more questions
	if number <= len(survey.questions):
		# Check if its the fiirst question (which will not have any answer(s) yet.)
		if number >=2:
			responses.append(request.form.get('answer', 'None'))
			session['answers'] = responses
		return render_template('questions.html', survey=survey, number=number)
	
	# If this was the last question:
	else:
		responses.append(request.form.get('answer', 'None'))
		session['answers'] = responses
		return render_template('thanks.html')

@app.route('/start')
def start():  
		global survey
		choice = request.args.get('choice')
		print('choice:', choice)
		survey = getattr(surveys, choice)
		print('survey:', survey)
		return render_template('start.html', survey = survey)

	