====================
Adding Question Page
====================

This page is slightly more complicated as it contains an html form, which
can produce different situations depending on the user's actions. A form 
requires that the POST method is used for data transfer, whereas to create a 
form the GET method is sufficient (the GET method was being used up to now, it
is the default method). We can use the two methods to
determine if the user arrived at the answer directly or after answering a
question. 

When using POST, Flask requires a secret key, this can be placed
directly in the application file (*bird.py*) or separately in a configuration 
file (*config.py*), the latter will be used here. Create *config.py* in the 
*venv* directory where *bird.py* is::

   import os
   
   class Config:
      SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

.. sidebar::   os is part of Python

   os is a core module of Python, so need not be installed.

Now *bird.py* needs to be modified to read the configuration file::

   from flask import Flask
   from flask import render_template
   from config import Config
   
   app = Flask(__name__)
   app.config.from_object(Config)
   .....

Check that the configuration works as expected, startup python locally::

   >>> from bird import app
   >>> app.config['SECRET_KEY']
   'you-will-never-guess'

Success! As we are only going to use the most basic ``form`` we do not require 
any additional help from an import such as Flask-WTF. Begin by modifiying
*bird.py* which will need a new route to the the question page *quiz.html*.
By now your files should be as follows::

         Flask
         ├──templates
         │  ├──index.html
         │  └──base.html
         │
         ├──venv
         ├──bird.py
         └──config.py

When a user is required to enter information there can be one of three results,
correct, incorrect or error. Incorrect is not an error, it is just wrong and
requires a different action to a correct answer. An error could be an incomplete
or empty entry. If correct or incorrect then we leave the question page and enter
the answer page. With an error the user remains on the question page and receives
a warning after which they can retry.

First we need some dummy data within *bird.py* to emulate a question and answer. 
Then we can
compose the actions of the application, before applying it to a template::

   ....
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
   ....

Now *bird.py* requires the route to the question page(*quiz.html*), it is 
used twice - in the first pass *quiz.html* is rendered the user answers
this is used in the second pass which then renders
the answer page (*result.html*). In the first pass it uses the
GET method and builds the form using a single line from our dummy data *quizlet*,
later this will be from the database. The dummy data for the question and answer 
is passed from *bird.py* to *quiz.html*, the bird song is processed into a
Jinja2 address before being passed to the question page.

When the user puts an answer into the form and submits it - 
the POST method is used. This becomes 
the second pass through *quiz*, compare the *user_answer* to the 
*correct_answer* to determine whether the user is correct or not, and
send to *result.html*. First edit *bird.py*::

   from flask import render_template, request, url_for
   ....
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
         # Determine if the answer is correct
         score = 1 if user_answer == correct_answer else 0
         # Render the result template with feedback
         return render_template('result.html', correct=score==1, correct_answer=correct_answer)
   # Retrieve a single row from quizlet later the database
   select = quizlet[0]
   soundfile = select['song']
   sound = url_for('static', filename=soundfile)
   return render_template('quiz.html', select=select, sound=sound)

.. sidebar::   The odd arrangement for the two methods in quiz.

   The POST method is only activated after a question has been answered, the
   GET method renders *quiz.html* so must be called first. However we don't
   want the page rendered twice, when answered we come back to the *quiz route*
   with POST and compare the answers then go to *result.html*.

All the templates which follow are built using *base.html*, just
as was done for *index.html*. Within the body of *quiz.html*
we first need to inform the user where they are, they will then be asked the
question made ready by *bird.py* on the *quiz.route*. The question 
consists
of first playing the song, whose address is in the *sound* variable. Next
the question text is shown *select[query]* and the user invited to give their
answer. The form is built, which in our case is a single entry standard text 
type, at the end is a submit button which will send the answer back to the 
*bird.py* also at the *quiz.route*. There are 2 form values necessary,
the first is named *question_id* which is a hidden type, the 
second is *user_answer*. Create *quiz.html* in the *templates* folder::

   {% extends "base.html" %}

   {% block content %}
      <h2 class="text-center">Quiz Question</h2>
      <p>First play the audio</p>
         <audio controls>
            <source
              src={{sound}}
              type="audio/mpeg"
            />
            <source
              src={{sound}}
              type="audio/wav"
            />
            Audio not supported
         </audio>

      <div class="bird-form">
         {% if select %}
            <p>{{ select['query'] }}</p>
            <form method="POST" class="form">
               <input type="hidden" name="question_id" value="{{ select['id'] }}" >
               <input type="text" name="user_answer" class="form__input" 
                  placeholder="Your answer" required 
                  oninvalid="this.setCustomValidity('Put your answer here')" 
                  oninput="this.setCustomValidity('')" 
                  title="Put your answer here" autocomplete="off">
               <div class="centre">
                  <button type="submit" class="button blue">Submit</button>
               </div>
            </form>
         {% else %}
            <p class="text-muted">No questions available.</p>
         {% endif %}
      </div>
   {% endblock %}

The form has several methods that need to be followed. 

The input *type* ="text"
   Does what it says - the most straightforward method. 

*placeholder*
   The text that appears in the empty form. 

*label* 
   is a caption of that form element and shows all the time. 

*oninvalid* 
   is the text that shows when an error is made, in our case submitting an 
   empty field. 

*autocomplete* is set to *off* 
   this prevents previous answers showing up in later sessions.

Form File Updates
-----------------

Only config.py has been given, because the major changes to *bird.py* affect
unmade files, the new files quiz.html, result.html and final.html will be
shown in the next chapter.
