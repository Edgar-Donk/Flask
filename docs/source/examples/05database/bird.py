from flask import Flask
from flask import render_template, request, url_for, session
from config import Config
import sqlite3

app = Flask(__name__)
app.config.from_object(Config)

# Function to establish database connection
db_connection = lambda: sqlite3.connect("mydb.db")

@app.route('/')
def index():
    session.pop('count', None)
    session["count"] = 1
    return render_template('index.html', title='Home of the')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if session["count"] > 5:
        return render_template('final.html', title='End of')
    if request.method == 'POST':
        question_id = request.form.get('question_id')
        user_answer = request.form.get('user_answer').strip().title()
        # Fetch the correct answer from the database
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT answer FROM birdquiz WHERE id = ?", (question_id,))
        correct_answer = cursor.fetchone()[0].strip().title()
        cursor.close()
        conn.close()
        score = 1 if user_answer == correct_answer else 0
        session["count"] += 1
        return render_template('result.html', correct=score==1,
                correct_answer=correct_answer, title='Result')

    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, question, song FROM birdquiz WHERE id = ?", (session["count"],))
    select = cursor.fetchone()
    conn.close()
    soundfile = select[2]
    sound = url_for('static', filename=soundfile)
    return render_template('quiz.html', select=select, sound=sound, title='Question')
