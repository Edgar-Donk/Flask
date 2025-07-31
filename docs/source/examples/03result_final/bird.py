from flask import Flask
from flask import render_template, request, url_for
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

quizlet = [{'id': 1,
            'query': 'Question One',
            'ans': 'sparrow',
            'song': 'Song One'},
        {'id': 2,
            'query': 'Question Two',
            'ans': 'hawk',
            'song': 'Song Two'}
        ]

@app.route('/')
def index():
    return render_template('index.html', title='Home of the')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # The user is using form
        # Retrieve user's answer and corresponding question ID
        user_answer = request.form.get('user_answer').strip().title()
        # the answer has any leading and trailing blanks removed
        # the answer is made into title format (leading capital)
        # Fetch the correct answer from the dummy data
        correct_answer = quizlet[0]['ans'].strip().title()
        #print(correct_answer)
        # Determine if the answer is correct
        score = 1 if user_answer == correct_answer else 0
        # Render the result template with correct_answer feedback =score==1 later
        return render_template('result.html', correct=score==1, correct_answer=correct_answer)
    # Retrieve a single row from the dummy data
    select = quizlet[0]
    soundfile = select['song']
    sound = url_for('static', filename=soundfile)
    return render_template('quiz.html', select=select, sound=sound)