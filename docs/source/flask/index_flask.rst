Flask Index
===========

What to Expect
--------------

.. |home| image:: ../figures/home_page1.avif
   :width: 129
   :height: 52
   :alt: home page

.. |dupl| image:: ../figures/account_duplicate1.avif
   :width: 102
   :height: 114
   :alt: account duplicate name

.. |acc| image:: ../figures/account2.avif
   :width: 98
   :height: 109
   :alt: account

.. |quiz| image:: ../figures/quiz2.avif
   :width: 101
   :height: 107
   :alt: quiz

.. |corr| image:: ../figures/result_correct1.avif
   :width: 102
   :height: 187
   :alt: correct result
   
.. |incorr| image:: ../figures/result_incorrect1.avif
   :width: 100
   :height: 187
   :alt: incorrect result

.. |final| image:: ../figures/final1.avif
   :width: 99
   :height: 95
   :alt: final

+---------+---------+-----------+--------+--------+----------+---------+
| |home|  |  |acc|  |  |dupl|   | |quiz| | |corr| | |incorr| | |final| |
+---------+---------+-----------+--------+--------+----------+---------+
| index   | account | duplicate |  quiz  | right  |  wrong   |  final  |
+---------+---------+-----------+--------+--------+----------+---------+

By the time we have reached *Styling Form* our web pages should
look like the images above.

index
   The home or starting page

account
   Load the user name, using a form

duplicate
   The reaction when a user tries to insert a duplicate user name

quiz
   Ask a question after playing a bird song

right
   The result page showing the reaction to a correct answer

wrong
   The result page showing the reaction to an incorrect answer

final
   The last page giving the user their final score, and how well they did

We then apply some styling, which helps to keep the end-users interest, this
is where you can also inject your own styling without affecting the basic
structure and design.

Finally we make the system into an executable program using Python's virtual
environment, venv.

.. toctree::
   :maxdepth: 3
   :caption: Contents:
   
   using_flask_setup
   using_flask_first_steps
   using_flask_form
   using_flask_result_final
   using_flask_session
   using_flask_database
   using_flask_users
   using_flask_style
   using_flask_style_form
   using_flask_background
   using_flask_venv
