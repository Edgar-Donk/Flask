Elements in Line
================

In HTML there are different ways to keep elements in line, the problem comes
when we require several smaller elements, our thumbnails, and the selected
image which will be much larger and out of line. If the hero image is portrait
then it makes sense to have the thumbnails in column, whereas if the large 
image is landscape then the thumbnails would be better displayed in a row.

According to `W.S.Toh <https://code-boxx.com/keep-html-elements-on-same-line/>`_
the methods are as follows:-

Flex
   One of fastest and easiest with additional controls. 

Grid
   Maybe better as we control the layout using *fr* (a bit like tkinter's
   grid method).

Table
   Rather *funky method*.

Float
   Required a clearfix container - semi-hack in horizontal line but would be
   even more of a problem in the vertical column.

Inline-Block
   Required a dummy comment in the HTML to work in line. In column mode it
   is even worse.

Flex works well in one dimension, row *or* column, on the other hand grid is 
made for a two dimension situation row *and* column.

Different Elements
------------------

How an element behaves is primarily influenced by its inate block or inline
characteristic, so an image has to be treated differently to text.