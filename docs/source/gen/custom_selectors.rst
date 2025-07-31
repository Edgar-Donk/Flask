Custom Selectors
================

Selectors are one of the methods that we can style or animate the html. See 
how a great many websites are based on the following::

   <!DOCTYPE html>
   <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <title>Title</title>
      </head>
      <body></body>
   </html>

The part that is standardised sections are clearly
demarcated, whilst in the customised part <body>, it's a bit of a free-for-all.
Many websites use a mixture of <div> and <span> combined with *class* to
distinguish which <div> or <span> is being selected in css or javascript. It is 
not too clear where one section starts and finishes or which parts are 
dependancies to which part. How often have you used a text editor to show
the dependancy of the closing </div>. Compare to the webpage start <html>,
<head> and <title> each has its own individual closure.

A slight improvement is to use radio buttons or unordered lists
(bullet points) as a framework. 

`Matthew James Taylor <https://matthewjamestaylor.com/div-custom-elements>`_
makes a forceful case for custom tags. Essentially a custom tag acts like
the inline tag <span> if required for page structure, like <div>, then
the custom tag has to be set to display a block::

   my-custom-tag {
      display: block;
   }

.. sidebar:: Block Structure

   Often the css implies this already, so the display block is not 
   always required.

Using Custom Tags
-----------------

Use built-in tags
   html has `a host of meaningful tags <https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements>`_
   where applicable use these.

No capital letters
   That is no uppercase ASCII characters.

Must contain one or more hyphens
   *my-container* is valid, *container* is invalid.

Start with lowercase letter
   Can contain numbers, UTF-8 characters even emojis.

Always supply a closing tag
   Use </my-el> after <my-el>

Define the custom tags.
   At the <body> start list all the custom tags followed by their closing tags.

The custom elements require no special characters when reading with css - in
fact just like <span>. The difference is that we can make our tag more meaningful,
so some classes will be redundant.

Registration
------------

Matthew James Taylor states that registration is not required, however 
definition is necessary, when
`checking on <https://validator.w3.org/check>`_ each of the custom tags 
had an error of *undefined element*. After listing the tags, the HTML was
validated.

If the custom tags are being used for more complicated behaviour than
just replacing <span> or <div> then registration is required. Mozilla has a
utility `X-Tag <https://www.x-tags.org/>`_ to help with the registration.
