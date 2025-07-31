====================
First Steps in Flask
====================

*venv* can access Python but none of the Python external packages found in 
*site-packages*.
We will need to install Flask using *cmd.exe* running in the venv
environment. These imports stay separate from the normal Python imports. First 
of all ensure that *cmd* is inside the *venv* environment *cmd* shows::

   (venv) C:\.....\Flask> 

and install Flask::

   pip install Flask

.. sidebar:: Use the Correct pip.

   If cmd is not in the virtual environment then Flask will be installed in 
   Python, which is not required for this exercise.

This will install Flask inside *venv* in the subdirectory *Lib\site-packages*,
where *pip* was already installed when the virtual environment was created.

As the application is small we only need a single control file. The 
name of the Python file is of our choosing so let's call it *bird.py*
rather than the often used *app.py*. First check that everything works as 
expected. Make a simple file in the *Flask* directory, bird.py, with just 
a single path that says *Hello world*::

   from flask import Flask # import the Flask module
   
   app = Flask(__name__) # create instance of the class

   @app.route('/') # Flask decorator used to show route, in this case default path
   def hello_world(): # creating a function that works with the default path
      return 'Hello, World!'

.. sidebar:: Placing *flask run*.

   If we had placed the *flask run* within our
   Python file we could not have tested the program with a python GUI using
   *run* (Python run) without starting Flask as well. 
   
   This way we can check that the Python 
   has no obvious problems, otherwise we must wait for the results from our 
   Flask server to show up errors.

Start up Flask, by typing the following in *cmd* that is sitting in the *venv* 
environment::

   flask --app bird run --debug

Which should give our *Hello World!* 

*cmd* now shows::

   * Serving Flask app 'bird'
   * Debug mode: on
   WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
   * Running on http://127.0.0.1:5000

Open up a web browser, such as *Firefox*, *Opera*, *Chrome*, etc ....
Create a new tab, put in the address *http://127.0.0.1:5000* and now 
*Hello World!* should be displayed. 

If we wish to stop the Flask server simply type <ctrl C> (
type control key and c together), then confirm. To restart type in the command
used before or create a batch file *start.bat*::

   flask --app bird run --debug

Working with HTML Files
-----------------------

The first html file we create will welcome the user to the bird quiz ,
let's call it *index.html*, like many start sites in Flask. Change *bird.py*
to render the template::

   from flask import Flask
   from flask import render_template # import flask module render_template
 
   app = Flask(__name__)

   @app.route('/')
   def index():
      return render_template('index.html')

.. sidebar:: @app.route('/')

   @app.route is the Flask decorator that maps URL paths to view 
   functions. It's how Flask knows which function to execute when a specific 
   URL is requested. The ('/') by default maps to the start side, where the
   web browser has logged onto using the web address given by the Flask server.

Create a *templates* folder::

      Flask
         ├──templates
         │  ├──index.html
         │  └──base.html
         │
         ├──venv
         bird.py
         start_venv.bat
         stop_venv.bat
         start.bat


Now make the file *index.html* and place it in the *templates* folder::

   <!DOCTYPE html>
   <html lang="en">
   <head>
      <meta charset="UTF-8">
      <title>Bird Quiz</title>
   </head>

   <body>
      <h1><font color="#ff073a">Welcome to the Bird Song Quiz.</font></h1>
      <br>
      <h2><font color="#ff073a">How good are you on bird songs?</font></h2>
    
   </body>
   </html>

Check out the flask server, it will show that it detected a change in *bird.py*
and that it restarted - this is normal behaviour when the debugger is active.

Refresh 'http://127.0.0.1:5000'.

It should change from "Hello World!" to "Welcome to the Bird Song Quiz" and
"How good are you on bird songs?".
Nothing to get excited about, except we need to improve the styling. Note that
the browser tab no longer reads ``http://127.0.0.1:5000`` but ``Bird Quiz``.

But let's
first start using some of the power of Jinja2 and improve index's functionality.

Working with Jinja2
-------------------

To date html has no inbuilt method to include conditional
clauses, Flask comes with `Jinja2 <https://jinja.palletsprojects.com/en/stable/>`_ 
and this allows us to have conditional clauses.
Modify the title block of *index.html* so that it has a default value and one
that can be modified from the route's return statement (found in bird.py)::

      {% if title %}
      <title>{{title}} Bird Quiz</title>
      {% else %}
      <title>Welcome to Bird Quiz</title>
      {% endif %}

.. sidebar:: Jinja2 Conditional Clauses and Variables.

   Our conditional clauses started and finished with {% ... %}, and contained
   if, else and endif as the conditional commands, endif is required to finish
   off the commands. Inside the conditional clauses we can refer to variables
   initiated within the control file *bird.py*, in this case *title*, but 
   within html
   the variable is enclosed in double curly brackets {{title}}.

After the template change reload our website, the main body remains unaltered,
but the browser tab changed from *Bird Quiz* to *Welcome to Bird Quiz*. Change
the *index* function in *bird.py* to add the title variable and its value::

   def index():
      return render_template('index.html', title='Home of the')

The server should have automatically restarted and our web page's tab should 
now be *Home of the Bird Quiz* after being refreshed. 

Next let's use template inheritance to help build future templates without as much
duplicated code. A base html with common code is created within the *templates*
directory, which we shall call
*base.html* (nothing but original). Also let's include a link back
to our welcoming page at *index.html*, at any stage the user should be able
to reset (stop or restart), this will be the normal html link <a></a> block.
Use the Jinja2 *url_for()* method to create the link.  
Add a blockcontent and an endblock statement in which the
templates each have its own content. 

*base.html* will copy most of *index.html*
apart from the content within the *body*::

   <!doctype html>
   <html>
      <head>
        <meta charset="UTF-8">
         {% if title %}
         <title>{{ title }} Bird Quiz</title>
         {% else %}
         <title>Welcome to Bird Quiz</title>
         {% endif %}
      </head>
      <body>
         <div>Bird Quiz: <a href="{{ url_for('index') }}">Reset</a></div>
         <hr>
         {% block content %}{% endblock %}
      </body>
   </html>

Now it is possible to simplify *index.html* and subsequent templates::

   {% extends "base.html" %}

   {% block content %}
      <h1><font color="#ff073a">Welcome to the Bird Song Quiz.</font></h1>
      <br>
      <h2><font color="#ff073a">How good are you on bird songs.</font></h2>
   {% endblock %}  

We started off by building upon *base.html* using *extends*, then the unique
content is given within the *block content*. We can now refresh the browser page,
it and the tab should remain unchanged apart from the addition of the *Reset*
link made in the body of *base.html*. Also note that the Flask server continued
running but found the changed index.html with a return code of ``200`` which 
is successful.

.. sidebar:: Block and Extends

   Jinja2 uses a similar notation to its conditional clauses for *block*
   and extends, in that the clause is enclosed in curly brackets with a percent
   sign {%...%}. The file it points to in *extends* is enclosed in quotation
   marks. *block content* closes with an *endblock*.

File Updates
------------

start.bat, bird.py, index.html and base.html will be found in 
*examples/01first_steps*.
