class Question:
    """Question on a questionnaire."""

    def __init__(self, question, choices=None, allow_text=False):
        """Create question (assume Yes/No for choices."""

        if not choices:
            choices = ["Yes", "No"]

        self.question = question
        self.choices = choices
        self.allow_text = allow_text


class Survey:
    """Questionnaire."""

    def __init__(self, title, instructions, questions):
        """Create questionnaire."""

        self.title = title
        self.instructions = instructions
        self.questions = questions


satisfaction_survey = Survey(
    "Customer Satisfaction Survey",
    "Please fill out a survey about your experience with us.",
    [
        Question("Have you shopped here before?"),
        Question("Did someone else shop with you today?"),
        Question("On average, how much do you spend a month on frisbees?",
                 ["Less than $10,000", "$10,000 or more"]),
        Question("Are you likely to shop here again?"),
    ])

personality_quiz = Survey(
    "Rithm Personality Test",
    "Learn more about yourself with our personality quiz!",
    [
        Question("Do you ever dream about code?"),
        Question("Do you ever have nightmares about code?"),
        Question("Do you prefer porcupines or hedgehogs?",
                 ["Porcupines", "Hedgehogs"]),
        Question("Which is the worst function name, and why?",
                 ["do_stuff()", "run_me()", "wtf()"],
                 allow_text=True),
    ]
)

python_quiz = Survey(
    "Ralph's Python Test",
    "Let's check your Python knowledge",
    [
        Question("When was Python created?",
                 ["1991", "2001", "2011"]),
        Question("Who created Python?",
                 ['Paul "Python" Petterson', 'Guido van Rossum', 'Jeff Bezos']),
        Question("Is Python named after the python snake?"),
        Question("Does Python run on the server?"),
        Question("Which is better, Python, JavaScript, or another language, and why?",
                 ['Python', 'JavaScript', 'other language'],
                 allow_text=True)
    ]
)

surveys = {
    "satisfaction": satisfaction_survey,
    "personality": personality_quiz,
    "python": python_quiz,
}