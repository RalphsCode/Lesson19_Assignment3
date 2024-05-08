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
	global responses
	# Check if its the fiirst question (which will not have any answer(s) yet.)
	if number >=2:
		responses.append(request.form.get('answer', 'None'))
		if request.form.get('comment'):
			responses.append(request.form.get('comment'))
		session[survey.title] = responses
	# Check if there are any more questions
	if number <= len(survey.questions):
		return render_template('questions.html', survey=survey, number=number)	
	# If this was the last question:
	else:
		responses = []
		return render_template('thanks.html')

@app.route('/start')
def start():  
		global survey
		choice = request.args.get('choice')
		survey = getattr(surveys, choice)
		return render_template('start.html', survey = survey)

	