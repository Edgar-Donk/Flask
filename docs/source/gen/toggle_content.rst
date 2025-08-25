================
Hide Show Toggle
================

Within Sphinx there are several methods to hide and show content, which have 
different ways to load their applications. Within HTML there are yet more methods,
so the choice is large.

`Older methods <https://stackoverflow.com/questions/2454577/sphinx-restructuredtext-show-hide-code-snippets>`_ 
use Javascript coupled with CSS. The first method was used by myself this worked
well in spite of the setup procedure. It entailed adding a template in _templates
directory, adding some css in _static/custom.css. Adding a function in the conf.py
file also ensuring that _templates and _static have their respective methods 
initialised in conf.py.

At first this method worked well, but now the local sphinx on my machine
cannot make it work although ReadtheDocs continues to work.

Within this page other methods were mooted. Since then both Sphinx and HTML
have gone through several revisions and we can try these instead. Sphinx
appears to have adopted  Bootstrap under the 
`sphinx_design <https://sphinx-design.readthedocs.io/en/latest/index.html>`_
to make resposive web components. This is activated by first installing through
*pip install sphinx-design* add the extension in conf.py::

   extensions = ["sphinx_design"]

*Dropdowns* are one of six components within sphinx-design. The problem with
dropdowns is that the icon showing toggling is at the 
righthand end of the line and does not stand out. It looks much like
hiddenCodeBlock another sphinx option.

Using HTML
----------

.. raw:: html
   
   <details>
   <summary style="color:#7787d2"> <i> Show/Hide Code </i> bird.py </summary>

.. literalinclude:: ../examples/01first_steps/bird.py
      :emphasize-lines: 6-8

.. raw:: html

   </details>

|

Meanwhile HTML has also produced its own version, which probably is the simplest
to install, all 
browsers `are compatible <https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details>`_ .

To use it one can use *raw html* within rst. Use a pair of html tags, *details*
and *summary*. *details* is the outer or parent tag and has the content that will
be hidden/shown, while *summary* acts as a switch or button - it contains an
icon on the left hand side that is a triangle that points horizonally when the 
content is hidden and downwards when the content is shown. On all browsers,
apart from *Safari*, this icon can be changed, if required.

.. note:: 

	The cursor should change to a pointer when it hovers over the text

Before the HTML is closed off we can insert some rst such as *literal include*
together with its methods such as highlighting specific lines. Edit the 
*summary* to inform the end user what is going on, this part is within html::

   .. raw:: html
   
   <details>
   <summary style="color:MediumSlateBlue"> <i> Show/Hide Code </i> bird.py </summary>

   .. literalinclude:: ../examples/01first_steps/bird.py
      :emphasize-lines: 6-8

   .. raw:: html

      </details>

The text is within the *summary* tabs, we want the text to stand out, so it 
is coloured.
The part that says *Show/Hide Code* is italicised, then comes the name of the
target, the full address is not required.

Leave an empty line and we are in sphinx rst code again. Place *literal include*
on the leftmost margin, show the target, this time with the full address and any
of the relevant `directives <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-option-literalinclude-class>`_ .
Then we can finish off with the *details* tag after a blank line.






