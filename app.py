from flask import Flask, request, render_template, redirect, flash, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
import surveys

# Globally scoped variables
responses = []
survey = {}
number_check = 1

app = Flask(__name__)

app.config['SECRET_KEY'] = "Ralph_01234"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/home')
def home():
	""" Home page 
	Users select from the available surveys. """
	survey_options = surveys.surveys
	return render_template('home.html', survey_options = survey_options)


@app.route('/start')
def start():  
		""" Start Page 
		Users are introduced to the survey, and click a start button to get started.
		Sends users to the questions page."""
		global survey
		# Find out which survey was chosen
		survey_choice = request.args.get('choice')
		if survey_choice == 'python':
			survey_choice = 'python_quiz'
		elif survey_choice == 'personality':
			survey_choice = 'personality_quiz'
		else:
			survey_choice = 'satisfaction_survey'
		# set the appropriate survey object into global scope
		survey = getattr(surveys, survey_choice)
		# Call the start survey page
		return render_template('start.html', survey = survey)


@app.route('/questions/<int:number>', methods=['GET'])
def questions(number):
	""" Questions Page
	presents each question and answer options on unique pages.
	The HTML page also saves the user answers to the Session.
	Once a question is answered, clicking the button reloads
	the question page with the next question."""
	global survey
	global responses
	global number_check

	if number != number_check:
		flash('You are not able to access that page directly. Here is the next question for you...')
		number = number_check
	# Present the next question
	return render_template('/questions.html', survey=survey, number=number)

	
@app.route('/answers/<int:number>', methods=['GET', 'POST'])
def answers(number):
	""" Answers Page
	The HTML page saves the user answers to the Session.
	Once a question is answered, clicking the button redirects
	to the question page with the next question."""
	global survey
	global responses
	global number_check

	number_check += 1

	responses.append(request.form.get('answer', 'Not answered'))
	if request.form.get('comment'):
		responses.append(request.form.get('comment', 'No Comment'))
	session[survey.title] = responses
	if number < len(survey.questions):
		# If there are more questions, present the next one
		return redirect(f'/questions/{number +1}')	
	else:
		# If this was the last question, reset the answers list, and go to thank you page:
		responses = []
		number_check = 1
		return render_template('thanks.html', survey_title = survey.title)