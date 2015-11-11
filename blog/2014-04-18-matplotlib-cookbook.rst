.. include:: ../header.txt
.. include:: ../footer.txt
.. include:: ./sidebar.txt
.. ----------------------------------------------------------------------------


Matplotlib Plotting Cookbook review
-----------------------------------
**April 20, 2014** - Nicolas P. Rougier

I've been invited to review the book `Matplotlib Plotting Cookbook
<http://www.packtpub.com/matplotlib-plotting-cookbook/book>`_ by Alexandre
Devert, published by Packt Publishing. The publisher sent me a free electronic
copy of the book. I'm not paid for writing this review and I'm not affiliated
with Packt Publishing. I declare no conflict of interest for this review.

|
|

**Structure of the book**

The book is organized in 8 chapters gathering a total of 69 recipes (9 more
than the book subtitle lower bound: *Learn how to create professional scientific plots
using matplotlib, with more than 60 recipes that cover common use cases*):

* **Chapter 1: First Steps** (14 recipes) describes some standard plots of the
  matplotlib packages (plots, bars, scatters, boxplots) with concise sources
  and standard output, using matplotib defaults settings.

* **Chapter 2: Customizing the Color and Styles** (14 recipes) describes how to
  change style the various elements of a plot (line color/width/style, marker
  type/size/color, fill color/pattern).

* **Chapter 3: Working with Annotations** (11 recipes) explains how to add text
  to a figure, be it an axis label, a title, an annotation, a legend or tick
  labels.

* **Chapter 4: Working with Figures** (7 recipes) describes different simple
  ways of layouting subplots (aspect ratio, axis sharing) between subplots and
  using different type of axis (logarithmic, polar, etc.).

* **Chapter 5: Working with a File Output** (5 recipes) explains the various
  options linked to the saving of the figure (formats, transparency, multipage).

* **Chapter 6: Working with Maps** (7 recipes) Despite the title, this chapter
  introduce concepts related to images and vector fields display.

* **Chapter 7: Working with 3D Figures** (6 recipes) presents the main 3D plots
  (scatter, lines, meshes, bars) as well as how to tweak different settings.

* **Chapter 8: User Interface** (5 recipes) introduces interaction throught the
  native matplotlib toolkit as well as mainstream toolkits (tkinter, gtk, wx)
  with the notable absence of qt.

Each recipes is organized around 4 paragraphs that are invariably:

1. | Recipes title
2. | How to do it...
3. | How it works...
4. | There's more

and each recipe is illustrated with a figure whose sources are provided within
the recipe.

|

**Review**

The preface of the book indicates that the book is intended for readers who
have some notions of Python and a science background. While the science
background is not an absolute necessity, it is true that one can use the book
using only some vague notion of a Python. Overall, this book is really a
cookbook that show precise examples of how to do basic things using matplotlib,
mainly slanted towards absolute beginners. While the `matplotlib gallery
<http://matplotlib.org/gallery.html>`_ is incredibly useful for most people, it
requires nonetheless some knowledge to be able to extract the useful
information from the different scripts. This book has the merit of organizing
several examples into themed chapters with precise explanations. Even if it
doesn't cover all the basic concepts of matplotlib, it might comes handy for
beginners, especially with the different displayed figures. For more advanced
users, the matplotlib gallery might be a better option that cover a wider range
of matplotlib capabilities.

Among the missing concepts, it is to be noted that nothing is said about maps
in spite of chapter 6 title (e.g., display a map of Europe with capitals), the
default matplotlib settings are only reviewed very briefly in chapter 2,
animations are not introduced at all and the overall quality of the different
figures is decent without being specifically beautiful. However, scripts have
been kept rather small and this may explain why author used mainly default
settings. At least for pie chart, author should have corrected the aspect
ratio. Furthermore, the interface chapter is lacking the qt toolkit which is
unfortunate given the popularity of this toolkit. Finally, the textual table of
matter would have benefited from a more visual one since each cookbook is
related to one figure and it would have facilitate the use of the cookbook.

My personal recommendation would be to buy the book only if you're a total
beginner in both Python and scientific visualization. For slightly more
advanced user, the matplotlib gallery might be a better option because it also
displays more up-to-date examples. Matplotlib being in active development, it
is of course quite difficult for such a printed book to give account of latest
development.
