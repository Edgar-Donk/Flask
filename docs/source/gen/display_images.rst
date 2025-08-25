Display Images
==============

Carousel
--------

.. note:: The following is for those writing in Sphinx, not the end user.

If you look up carousel for images, it's likely that someone will state that 
carousel for images is a thoroughly bad idea. There are however a plethora
of various examples on the internet as well as methods for their creation - 
so someone must think they are not so bad afterall.

Unfortunately only only 1 to 2% of the end-users, a fickle class if ever 
there was one,
continue to engage with the sites that use carousels, otherwise it's some
sort of Pavlovian reaction. 

1. See the carousel. 

2. Leave the site.

Truly it's as blunt as that.

Luckily there is a replacement that seems to work, and that is based on
scrolling that immediately reveals the content in a surprising way.

Warning
-------

.. warning:: Sphinx Carousel

   At some stage the sphinx carousel worked, but using the latest versions 
   of programs, there is a general failure - KeyError: 'classes' in sphinx.search.
   Apparently the problem is still outstanding 12 March 2025 to 12 August 2025.

Pure CSS Horizontal Scrolling
-----------------------------

This is a workaround in HTML. It avoids the dangers of a carousel - equally
there are Cassandras who say that the average punter cannot deal with horizontal
scrolling as they are only used to vertical scrolling - there are an increasing
number of websites using horizontal scrolling and winning awards.

.. sidebar:: Using the Scrollbars

   To make the scrollbar appear - nothing magic here - just reduce the window 
   size until the scrollbar appears.
   
   Normally the contents can be viewed above and below the current display
   by moving the vertical scrollbar or clicking in the scrollbar trough above 
   or below the scrollbar. If the mouse is anywhere in the active window the
   contents shift up or down when the mouse scroll wheel is used.
   
Horizontal scrolling can be controlled with Javascript but it suffers because
it has to control the scrolling in a system hungry fashion - if we can do it
purely in CSS the browser can make it happen without anymore resources than for 
an ordinary scroll.

First we have to fool the browser into thinking it is scrolling vertically when in
fact it is scrolling horizontally. To enable scrolling the content must
overflow the user window. The effect is heightened if the scrollbar, which
would be normally displayed, is switched off, but scrolling is enabled. 

Assume the images will be displayed inside a rectangular container, long
sides vertical,
which will be rotated through 90°. As the
container is turned its sides will move relative to their original position.
Rotate about one of the upper corners so that the container's long
side is now horizontal at the same level as the upper corner. If we rotate
anticlockwise (-90°) and use the top right corner, then the upper side will
be the same distance away from the top margin as a short side used to be. 
The short side closest to the left hand margin will now be further away than the
long side used to be by an amount equal to the width of the container.

The container will normally end up being too far from the left hand margin, 
which will
require moving the container sideways (translate), make the translation first 
and remember to use
a minus **Y** for a minus **X** translation.

.. sidebar:: Transform - Rotation and Translating

   The css command transform allows both rotation and translation to occur
   sequentially. The order affects the outcome, if translate precedes rotate
   then the element moves along the original main x or y axis, but if translate
   follows rotate then it moves along the rotation axis::
      
      .one {
         transform: translateX(200px) rotate(135deg);
      }
      
   Check out the Transform Order at `mdn <https://developer.mozilla.org/en-US/docs/Web/CSS/transform#examples>`_

Meanwhile the childen (images) have also been rotated as they sit in the 
container. They will need to be rotated - this time clockwise 90°.


 