Virtual Environment - venv
==========================

The virtual environment was installed right at the beginning, now we have an
application that works and can be showed off - it is time to package the
application and run it as a free standing *exe* file. To package it first of
all install the *Auto Py to EXE*, ensure you are working in your *venv* 
directory and it is active::

   pip install auto-py-to-exe

First add a couple of lines to the end of *bird.py*, when made into an
executable the flask server will start when the exe file is run::

   # Run the Flask application if this file is executed directly
   if __name__ == '__main__':
      app.run(debug=True)

Next import Jinja2 at the start of *bird.py*, this helps resolve any problems
*auto-py-to-exe* may have with Jinja2::

   import jinja2.ext

Before running *auto-py-to-exe* it's best to change to a newly created 
subdirectory of *venv*. Activate *venv* then
just type into *cmd* *auto-py-to-exe*, this should bring up a gui 
interface (uses Chrome). The application actually uses pyinstaller under the
hood.

The first window is the *Script Location* which is the main Python file, which
in our case is *bird.py*. It is less work for the application if it becomes 
*One Directory*. Our application will be *Console Based* since we will run
the Flask server as well. If we have and want to add an *Icon* this is the next 
window. Then comes *Additional Files*, put all the templates and static files
here under their appropriate directories. Don't forget to include the database
as well.

When ready click on the big blue button at the end of the page. If all goes
well then after a few minutes the files and folders will be created. If there
is some problems then these should be resolved, if the file is huge then the
virtual environment was not used, also there are likely problems with pyqt5 and 
pyqt6. If you are unlucky the antivirus software might treat the whole exercise
as an attack, switch it off while running *auto-py-to-exe*.

There is no executive file supplied, you should use *auto-py-to-exe* yourself
since there may be times when you did need it in earest. 
