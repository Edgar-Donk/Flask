=====
Setup
=====

Bird Quiz
=========

There are many tutorials about using Flask on the internet, so one more 
shouldn't harm anyone. Most tutorials have to be general, so they choose a
simple topic like a blog. This will be different, let's make a quiz with
questions posed sequentially, our quiz plays a bird song then checks the user's
answer and shows whether it is correct or not and displays the correct answer
if wrong. At the start and end of the quiz are messages to the user welcoming
or encouraging to help the environment. 

If we had made this in Python then many of the operations would have been 
straightforward, but inside Flask the methods may need a bit of teasing out.
Flask allows the use of variables, but their life is often limited to their
immediate use. The styling of the web pages is a complete chapter in itself,
many handover this task to a third party (such as Bootstrap) but here we will
attempt to make it ourselves (with the aid of `W3Schools <https://www.w3schools.com/>`_ 
and `mdn Mozilla <https://developer.mozilla.org/en-US/>`_).

The questions were stored in an Sqlite3 database, which is part of the standard 
Python package.

Using a Virtual Environment (venv)
==================================

Working in a Python virtual environment is useful for long term projects, 
where the software stays at known releases, or where the Python script is to
be converted to an executable. One big advantage is that when converting to an
executable only the relevant modules are processed, this keeps the final file
at its smallest and needs considerably less processing time. 
In either case the venv can be readily installed 
and used. 

First make a new directory, say *Flask*. Open a command file (cmd.exe found 
in System32 on Windows), 
change the directory to the *Flask* directory [cd C:\.....Flask]. 

.. sidebar:: Ensure *cmd* is Readily Accessible.

   If cmd.exe is not yet installed on your *Desktop* now is a good time to put
   a shortcut to it there - unless you already are using an alternative.

*venv* is part of Python, so does not require installing. Start *venv* using 
*cmd* within the *Flask* directory:: 

   python -m venv venv 

After a small delay while directories and files are installed in the subdirectory
*venv* under our original *Flask* directory. 

Our venv environment will look like::
   
      Flask
         └──venv
            ├──Include
            ├──Lib
            ├──libs
            └──Scripts
               ├──activate.bat
               ├──deactivate.bat
               └──....
            pyvenv.cfg
      start_venv.bat
      stop_venv.bat

Start the virtual environment by calling *activate.bat* from *cmd* still
sitting in the *Flask* directory::

   .\venv\Scripts\activate

This should change how *cmd* shows where it is, from *C:\.....\Flask>* 
to *(venv) C:\.....\Flask>*.

To stop *venv* use *cmd* in the venv environment, still in the *Flask* 
directory::

   .\venv\Scripts\deactivate

Alternatively create the two batch scripts in the *Flask*
directory and start and stop the *venv* environment from there.

The two scripts start_venv.bat and stop_venv.bat are very similar, except for the 
commands *activate* and *deactivate*::

   .\venv\Scripts\activate

or::

   .\venv\Scripts\deactivate

Final Situation
---------------

There will be several html files within the templates directory: 

+--------------+---------------------------------------------------------+
|  File Name   | Purpose                                                 |
+==============+=========================================================+
| account.html | Shows and accepts user names for the quiz               |
+--------------+---------------------------------------------------------+
| base.html    | Uses template inheritance to simplify html files        |
+--------------+---------------------------------------------------------+
| final.html   | Last file which shows how well the user did             |
+--------------+---------------------------------------------------------+
| index.html   | First file to set up user                               |
+--------------+---------------------------------------------------------+
| quiz.html    | Question file that plays birdsong and shows environment |
+--------------+---------------------------------------------------------+
| result.html  | Shows result of question                                |
+--------------+---------------------------------------------------------+

To control these html files we require our Python files:

+--------------+-------------------------------------+
|  File Name   | Purpose                             |
+==============+=====================================+
| bird.py      | Overall controlling file            |
+--------------+-------------------------------------+
| config.py    | Configuration file for secret key   |
+--------------+-------------------------------------+

To create the database we used csv data, that contained the questions and
answers, together with the birdsong and background file 
names. This data was loaded into an empty database, which created the table
*birdquiz* from csv data. Another table *users* was then created in the 
database for the users.

+--------------+----------------------------------------------------+
|  File Name   | Purpose                                            |
+==============+====================================================+
| quizbird.csv | Data file of questions, answers and birdsong links |
+--------------+----------------------------------------------------+
| mydb.db      | sqlite3 database                                   |
+--------------+----------------------------------------------------+

In addition to these files several batch files were made to help with the
operation.

Keeping Track of the Changes
----------------------------

At various stages of the building of the application many of the files will
change, in particular *bird.py* and most of the html files, the names remain
unaltered but the contents change. To see the expected result and the reason
for the next change the actual version should be used.

Within the *examples* folder will be subfolders made according to the chapters
of *Using_flask* and the state of the used files at the end of the chapter.
As the application evolves the relevant files will be added or modified. This
chapter's files will be found in *00setup* under the *examples* directory, 
part of the *source* directory.