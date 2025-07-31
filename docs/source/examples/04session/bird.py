from flask import Flask
from flask import render_template, request, url_for, session
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
    session.pop('count', None)
    session["count"] = 0
    return render_template('index.html', title='Home of the')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        user_answer = request.form.get('user_answer').strip().title()
        correct_answer = quizlet[session['count']]['ans'].strip().title()
        score = 1 if user_answer == correct_answer else 0
        if session["count"] > 2:
            return render_template('final.html', title='End of ')
        session["count"] += 1
        return render_template('result.html', correct=score==1,
            correct_answer=correct_answer, title='Result ')
    select = quizlet[session["count"]]
    soundfile = select['song']
    sound = url_for('static', filename=soundfile)
    return render_template('quiz.html', select=select, sound=sound, title='Question ')
