from flask import Flask
from flask import render_template, request, url_for, session, redirect, flash
from config import Config
import sqlite3

def add(a, b):
    return (a or 0) + (b or 0)

app = Flask(__name__)
app.config.from_object(Config)

# Function to establish database connection
db_connection = lambda: sqlite3.connect("mydb.db")

@app.route('/')
def index():
    session.pop('count', None)
    session["count"] = 1
    return render_template('index.html', title='Home of the')

@app.route('/account', methods=['GET', 'POST'])
def account():
    if request.method == 'POST':
        conn = db_connection()
        cursor = conn.cursor()
        user_name = request.form.get('user_name').strip().title()
        try:
            conn = db_connection()
            cursor = conn.cursor()
            sqlite_insert_with_param = "INSERT INTO users (username) VALUES (?);"
            data_tuple = (user_name,)
            cursor.execute(sqlite_insert_with_param, data_tuple)
            conn.commit()
        except sqlite3.IntegrityError:
            print("IntegrityError during inserting data:")
            conn.rollback()  # Rollback in case of error
            error = f"User {user_name} is already registered."
            conn = db_connection()
            cursor = conn.cursor()
            accounts = conn.execute('SELECT username FROM users ORDER BY username COLLATE NOCASE ASC').fetchall()
            accounts = ', '.join([item for tupl in accounts for item in tupl])
            cursor.close()
            conn.close()
            flash(error,"error")
        else:
            # redirect for post
            session["username"] = user_name
            info = f"Well done {user_name} you have successfully made a quiz user!"
            flash(info, "info")
            return redirect(url_for("quiz"))
        return render_template('account.html', title='User', accounts=accounts)

    conn = db_connection()
    cursor = conn.cursor()
    accounts = conn.execute('SELECT username FROM users ORDER BY username COLLATE NOCASE ASC').fetchall()
    accounts = ', '.join([item for tupl in accounts for item in tupl])
    cursor.close()
    conn.close()
    return render_template('account.html', title='User', accounts=accounts)

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if session["count"] > 5:
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT username, tried, correct FROM users WHERE username = ?", (session["username"],))
        user_score = cursor.fetchone()
        cursor.execute("SELECT username, tried, correct FROM users WHERE correct = (SELECT MAX(correct) FROM users)")
        best_score = cursor.fetchone()
        cursor.close()
        conn.close()
        return render_template('final.html', title='End of', user_score=user_score, best_score=best_score)

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
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT tried, correct FROM users WHERE username = ?", (session["username"],))
        status = cursor.fetchone()
        try:
            conn = db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT tried, correct FROM users WHERE username = ?", (session["username"],))
            status = cursor.fetchone()
            update_query = """Update users set tried = ?, correct = ? where username = ?"""
            columnValues = (add(status[0],1), add(status[1],score), session["username"])
            cursor.execute(update_query, columnValues)
            conn.commit()
            cursor.close()
        except sqlite3.Error as error:
            print("Failed to update multiple columns of sqlite table", error)

        finally:
            if conn:
                conn.close()
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