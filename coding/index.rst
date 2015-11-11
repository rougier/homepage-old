.. include:: ../footer.txt
.. include:: ../header.txt
.. include:: ./sidebar.txt
.. ----------------------------------------------------------------------------



======
Coding
======

Here is a collection of software, libraries or recipes that I wrote for my own
purposes and that you might find useful as well. Unless stated otherwise,
permission is granted to copy, distribute and/or modify these software under
the terms of the `GNU General Public License
<http://www.gnu.org/licenses/gpl-3.0.html>`_ as published by the Free Software
Foundation; either version 3 of the License, or (at your option) any later
version.

Most of these projects are also available from my `github page <https://github.com/rougier>`_

|


Simulation
==========

Distributed Asynchronous Numerical & Adaptive computing
-------------------------------------------------------

.. image:: ../images/dana-1.png
   :class: img-round img-left
   :height: 100px

.. image:: ../images/dana-2.png
   :class: img-round img-left
   :height: 100px

.. image:: ../images/dana-3.png
   :class: img-round img-left
   :height: 100px

.. image:: ../images/DNF.png
   :class: img-round img-left
   :height: 100px

|

DANA is a python framework for distributed, asynchronous, numerical and
adaptive computing. The computational paradigm supporting the dana framework is
grounded on the notion of a unit that is a essentially a set of arbitrary
values that can vary along time under the influence of other units and
learning. Each unit can be connected to any other unit (including itself) using
a weighted link and a group is a structured set of such homogeneous units.

| → `DANA website <http://dana.loria.fr>`_
| → `Related article (Network: Computation in Neural Systems, 2012) <http://hal.inria.fr/docs/00/71/87/80/PDF/revision.pdf>`_


|


Neural field with finite propagation speed
------------------------------------------

.. image:: ../images/doughnut.png
   :class: img-round img-left
   :height: 100px

.. image:: ../images/DNF-delayed-2.png
   :class: img-round img-left
   :height: 100px

.. image:: ../images/DNF-delayed-3.png
   :class: img-round img-left
   :height: 100px

.. image:: ../images/DNF-delayed-4.png
   :class: img-round img-left
   :height: 100px

|

In collaboration with Axel Hutt, we've been studying the spatio-temporal
activity propagation which obeys an integral-differential equation in two
spatial dimensions that involves a finite transmission speed,
i.e. distance-dependent delays and derived a fast numerical scheme that allow
to quickly simulate numerically such equations. This python script implements
this numerical integration using python, numpy and scipy library.

| → `Sources <../downloads/DNF.py>`_
| → `Related article (Physical Review E, 2010) <http://hal.inria.fr/docs/00/53/30/67/PDF/paper.pdf>`_

|


Dynamic Self-Organization Maps
------------------------------

.. image:: ../images/DSOM-ring.png
   :class: img-round img-left
   :height: 100px

.. image:: ../images/DSOM-double-ring.png
   :class: img-round img-left
   :height: 100px

.. image:: ../images/DSOM-sphere.png
   :class: img-round img-left
   :height: 100px

.. image:: ../images/DSOM-cube.png
   :class: img-round img-left
   :height: 100px

.. image:: ../images/DSOM.png
   :class: img-round img-left
   :height: 100px

|

In collaboration with Yann Boniface, we designed a variation of the
self-organising map where the time-dependency learning function has been
replaced. This allows for on-line and continuous learning on both static and
dynamic data distributions. The newly proposed algorithm does not fit the
magnification law and the vector density is not proportional to the density of
the distribution as in most vector quantisation algorithms.

| → `Sources <../downloads/dynamic-som.tgz>`_
| → `Related article (NeuroComputing, 2011) <http://hal.inria.fr/docs/00/49/58/27/PDF/draft-revised.pdf>`_
| → `Online article using restructured text format (rst) <article/article.html>`_

|

Artificial Neural Networks
--------------------------

.. image:: ../images/neuron.png
   :class: img-round img-left
   :height: 100px

.. image:: ../images/MLP.png
   :class: img-round img-left
   :height: 100px

.. image:: ../images/ART.jpg
   :class: img-round img-left
   :height: 100px

.. image:: ../images/ANN.png
   :class: img-round img-left
   :height: 100px

|

Here is a list of some standard neural networks written in python. They were
made to be simple and useful for students. Each script is self-contained and is
around a hundred of lines. `Numpy <http://www.numpy.org>`_ is required for
simulation and `matplotlib <http://matplotlib.sourceforge.net>`_ for
visualization.

* | `Perceptron <../downloads/perceptron.py>`_
* | `Multi layer perceptron <../downloads/mlp.py>`_
* | `Elman recurrent network <../downloads/elman.py>`_
* | `Jordan recurrent network <../downloads/jordan.py>`_
* | Hopfield (not yet done)
* | `ART 1 <../downloads/art1.py>`_
* | `Self organizing map <../downloads/som.py>`_
* | `Neural gas <../downloads/ng.py>`_
* | Growing neural gas (not yet done)
* | `Voronoi <../downloads/voronoi.py>`_ (if you want to display the voronoi diagram).


|
|
|


Visualization
=============

Glumpy
------

.. image:: ../images/glumpy/galaxy.png
   :class: img-round img-left
   :height: 100px

.. image:: ../images/glumpy/tiger.png
   :class: img-round img-left
   :height: 100px

.. image:: ../images/glumpy/smoke.png
   :class: img-round img-left
   :height: 100px

.. image:: ../images/glumpy/protein.png
   :class: img-round img-left
   :height: 100px

.. image:: ../images/glumpy/text.png
   :class: img-round img-left
   :height: 100px



|

Glumpy is a python/OpenGL library for the fast vizualization of numpy arrays,
(mainly two dimensional) that has been designed with efficiency in mind.  If
you want to draw nice figures for inclusion in a scientific article, you'd
better use matplotlib.  If you want to have a sense of what's going on in your
simulation while it is running, then maybe glumpy can help you.

`→ glumpy website <http://glumpy.github.io>`_

|


SciGL
-----

.. image:: scigl/logo.png
   :class: img-round img-left
   :height: 100px

.. image:: ../images/scigl-4.png
   :class: img-round img-left
   :height: 100px

.. image:: ../images/scigl-1.png
   :class: img-round img-left
   :height: 100px

.. image:: ../images/scigl-2.png
   :class: img-round img-left
   :height: 100px

|

SciGL (Scientific OpenGL Visualization ToolKit) aims at facilitating the
development of scientific visualization by providing a set of C++ classes for
rapid prototyping of scientific visualization software. It has not been
designed as a library since the goal of SciGL is to try to offer a minimal set
of objects without the need for any kind of installation. A large number of
examples is provided to show how one can use parts of SciGL components to suit
its own needs.

`→ scigl website <./scigl/index.html>`_

|


GliPy, The OpenGL IPython/Python terminal
-----------------------------------------

.. image:: glipy/glipy.png
   :class: img-round img-left
   :height: 100px

.. image:: glipy/screenshot-8.png
   :class: img-round img-left
   :height: 100px

|

The goal of glipy is to create a comprehensive environment for interactive and
exploratory computing. To support this goal, glipy has two main components: an
interactive Python terminal and an architecture for embedding various graphical
elements directly within the terminal.

`→ glipy website <./glipy/index.html>`_

|


Terminal visualization
----------------------

.. image:: ../images/numpy_imshow.png
   :class: img-round img-left
   :height: 100px

Since modern terminals are able to handle up to 256 colors, it is thus quite
easy to visualize a 2-dimensional numpy array as long as it fits within the
terminal. It might come handy to quickly check how an array looks like.

`→ Sources <../downloads/numpy_imshow.py>`_

|
|
|

Python
======

Freetype python bindings
------------------------

.. image:: ../images/freetype-py.png
   :class: img-left img-round
   :height: 128

Python bindings for the FreeType library high-level API.

`→ Freetype bindings website <http://code.google.com/p/freetype-py>`_

|

Scientific Article using ReST
-----------------------------

.. image:: ../images/article.png
   :class: img-left img-round
   :height: 128

A modified rs2html.py to write a scientific article using the ReST format.

`→ Scientific ReST page <article/article.html>`_

|

AntTweakBar python bindings
---------------------------

.. image:: ../images/atb-python.png
   :class: img-left img-round
   :height: 128

atb-python offers python bindings for the `AntTweakBar
<http://www.antisphere.com/Wiki/tools:anttweakbar?sb=tools:anttweakbar>`_
library which is small and easy-to-use C/C++ library that allows programmers to
quickly add a light and intuitive graphical user interface into graphic
applications based on OpenGL, DirectX 9 or DirectX 10 to interactively tweak
their parameters on-screen.

`→ Sources <../downloads/atb-python.tgz>`_


|


Glydget, a pyglet GUI toolkit
-----------------------------

.. image:: ../images/glydget.png
   :class: img-left img-round
   :height: 128

Glydget is a(nother) pyglet GUI toolkit dedicated to "debugging" or scientific
computing. It is far from a complete GUI system (like kytten or simplui) but
rather aims at a quick and fast solution for displaying/editing variables and
pressing buttons.

`→ Sources <../downloads/glydget.tgz>`_

|

Pyroom
------

.. image:: ../images/pyroom.png
   :class: img-left img-round
   :height: 128

Pyroom is a fullscreen editor written in Python and GTK featuring full screen
multidocument text editor, small set of shortcuts, simple help page for
shortcuts and different styles / colorsets available.  More recent versions are
available at http://pyroom.org.

`→ Sources (GTK needed) <../downloads/pyroom.py>`_

`→ Pyglet version <../downloads/pyroom-pyglet.tgz>`_



|

Matplotlib gallery
------------------

.. image:: ../images/matplotlib-levels.png
   :class: img-left img-round
   :height: 100

.. image:: ../images/matplotlib-benchmark.png
   :class: img-left img-round
   :height: 100

.. image:: ../images/matplotlib-diseases.png
   :class: img-left img-round
   :height: 100

|

A matplotlib alternative `gallery <./gallery/index.html>`_

If you want to contribute, clone the gallery repository at
https://github.com/rougier/gallery and submit a pull request for a new example:

|

Wordle
------

.. image:: ../images/wordle.png
   :class: img-left img-round
   :height: 128

Inspired by the `wordle <http://www.wordle.net>`_ site, I made a quick try in
python using cairo, numpy and pyglet to get more or less the same result.  The
script allows you to save the image as well as a clickable map to link each
word to a specific link.  Code can be improved in a lot of different ways so
feel free to modify it.

`→ Sources <../downloads/wordle.py>`_

|

Python/Numpy, matrix extraction
-------------------------------

numpy extract is a small python script that allows to extract a sub-array
centered on a given position using a fixed shape, even it is out of bounds.

`→ Sources <../downloads/numpy_extract.py>`_

|

Numpy group
-----------

numpy group proposes an alternative implementation of record arrays using
contiguous block of memory. The design choice of numpy array layout is to
have data pointer points to one block of N items where each item is described
by the dtype. While it makes sense in most situation, it prevents record
arrays to have contiguous block of memory for each elementary dtype.

`→ Sources <../downloads/numpy_group.py>`_

|

Maze generator & path finding
-----------------------------

.. image:: ../images/maze.png
   :class: img-round img-left
   :height: 100px

.. image:: ../images/path-finding.png
   :class: img-round img-left
   :height: 100px

|

A maze generator python script and a path finding algorithm (using value
iteration).

| `→ maze.py <../downloads/maze.py>`_
| `→ path-finding.py <../downloads/path-finding.py>`_
| `→ maze example <../downloads/maze.npy>`_ (numpy array format)


|


C++/Boost/Python, build systems
-------------------------------

`Boost <http://www.boost.org>`_ provides free peer-reviewed portable C++ source
libraries.  You will find in the archive a set of boost python examples that
illustrate various boost mechanisms (as well as different build systems).

`→ Sources <../downloads/boost-python.tgz>`_


|

GLFW python bindings
--------------------

Python bindings for the `GLFW 2.4.7 <http://www.glfw.org/>`_ library.

`→ Sources <../downloads/glfw-python.tgz>`_

Binding for the 3.0 version are available from https://github.com/rougier/pyglfw

|
|
|

Miscellaneous
=============


OpenGL Freetype
---------------

.. image:: ../images/freetype-gl-1.png
   :class: img-left img-round
   :height: 100

.. image:: ../images/freetype-gl-3.png
   :class: img-left img-round
   :height: 100

|

OpenGL/FreeType is a simple engine for displaying a unicode text using a
(single) vertex buffer. The idea is simply to tightly pack every necessary
glyphs into a single texture and to generate a single vertex buffer to draw the
text.

| `→ Freetype-gl website <http://code.google.com/p/freetype-gl/>`_
| `→ Related article (Journal of Computer Graphic and Techniques, 2012) <http://jcgt.org/published/0002/01/04/paper.pdf>`_


|

Emacs octicons
---------------

.. image:: ../images/octicons-modeline.png
   :class: img-round img-left
   :height: 24px

|

The octicon font by github (https://github.com/styleguide/css/7.0) provides
some nice icons embedded in a font. This `package
<https://github.com/rougier/emacs-octicons>`_ gives an easier access to them
and must be used with the relevant face (octicons).


|

Emacs powerline
---------------

.. image:: ../images/emacs-powerline.png
   :class: img-round img-left
   :height: 100px

|

Inspired by the VIM powerline, I've coded a small powerline-like for
emacs. Original sources are available from the `emacswiki
<http://www.emacswiki.org/emacs/PowerLine>`_. Since then, Donald Ephraim has
rewritten this package and `his version
<https://github.com/milkypostman/powerline>`_ uses many of the techniques in
the original but tries to make it easier to add new things


|

Hills screensaver
-----------------

.. image:: ../images/hills.png
   :class: img-left img-round
   :height: 100

.. image:: ../images/hills-osx.png
   :class: img-left img-round
   :height: 100

|

Hills screensaver let you gently drift over rolling grassy hills, using ARB
multitexture, heightmap and lightmap. It requires SDL and OpenGL and should
work with xscreensaver and gnome-screensaver.

`→ Sources <software/hills-linux.tgz>`_

Chris Kent has ported hills to OSX and made a screensaver out of it (`sources
<software/hills-osx.zip>`_). Nick Ziztmann has since released an updated
version on http://seiryu.home.comcast.net/~seiryu/savers.html and sources are
available on `github <https://github.com/nickzman/hills>`_.

`→ Sources <http://seiryu.home.comcast.net/~seiryu/software/Hills1.3.dmg>`_

|

GNUBiff
-------

.. image:: ../images/gnubiff.png
   :class: img-round img-left
   :height: 64px

.. image:: ../images/gnubiff-2.png
   :class: img-round img-left
   :height: 64px

|


GNUBiff is a mail notification program that checks for mail and displays
headers when new mail has arrived. GNUbiff features include multiple mailbox
support, pop3, apop, imap4, mh, qmail and mailfile support, SSL & certificates
support, GNOME & GTK support and many other features.

`→ gnubiff website <http://gnubiff.sourceforge.net>`_

|
|


Outdated
========

While these software are certainly outdated and may not run on modern linux
distributions, they may be useful for code study. Of course, you're welcome to
adapt them and send me the new code...


GLPython, an OpenGL oriented python shell
-----------------------------------------

.. image:: ../images/glpython.png
   :class: img-round img-right
   :height: 100px

glpython is an OpenGL oriented python shell designed for efficient interactive
work with all major GUI toolkits in a non-blocking manner as well as a library
to build customized OpenGL objects using python as the basic language. GLPython
relies on backends such as GTK, WX, SDL or Qt that are able to open an OpenGL
context and handle keyboard and mouse events when necessary

`→ Sources <../downloads/glpython.tgz>`_

|


PyCons, GTK python console
--------------------------

.. image:: ../images/pycons.png
   :class: img-round img-right
   :height: 100px

pycons implements a python (or ipython) shell within a GTK window and handles
python stdin/stderr/stdout redirection and system wide stdout/stderr
redirection (using a pipe), provides history based on the GNU readline package
and automatic completion. It is also able to display matplotlib figures inline.
Each call to the show functions actually produces a FigureCanvasGTKAgg that is
inserted within the console.  A 'replot' command has been added that replot the
last figure.

`→ Sources <../downloads/pycons.tgz>`_

|

SDL Terminal
------------

.. image:: ../images/SDL-terminal-1.png
   :class: img-round img-right
   :height: 100px

SDL Terminal is a library that allows to have a pseudo-ansi color terminal that
can be used with any SDL application (with or without OpenGL). The internal
terminal surface is an SDL surface that is mapped to a texture when OpenGL is
used (and then it is quite simple to use the texture to map it on any GL
surface, like in the glcube example from distribution).  Any user input raises
an SDL_TERMINALEVENT that can be catched like any other SDL event and the event
structure holds the user actual input.

`→ Sources <../downloads/SDL-Terminal.tgz>`_

|

Boom !
------

.. image:: ../images/boom.gif
   :class: img-round img-right
   :height: 100px


Boom is a partial port of a Delphi/OpenGL demo made by Thomas Jahn. I only
ported the particle engine to C++/SDL/OpenGL to get the very nice explosion
Thomas designed.  The soft is called "boom" since it basically displays an
explosion every 5 seconds (with sound).  It requires SDL and OpenGL libraries
and it is supposed to be working indifferently on linux, mac os or windows
(using DevC++).

`→ Sources <../downloads/boom.tgz>`_

|

GTK Object view
---------------

.. image:: ../images/gtk-object-view.png
   :class: img-round img-right
   :height: 100px

GTK Object view uses Python self introspection capability to display any object
attributes with the possibility to edit them and supports undo/redo operations.

`→ Sources <../downloads/gtk-object-view.tgz>`_

|

Kohonen maps
------------

.. image:: ../images/kohonen-old.png
   :class: img-round img-right
   :height: 100px

Kohonen is an old version of the self-organizing map (SOM). This one has been
coded in C++ and run under windows or linux.

`→ Sources <../downloads/kohonen.zip>`_

|

Pets
----

.. image:: ../images/pets-1.png
   :class: img-round img-right
   :height: 100px

Pets is a port of an old program by Masayuki Koba where a cute tiny kitty was
following your mouse all over the screen. This new version is base on gtk and
uses an xml description for animations.  There is also another animation with a
tiny tux (see the Artwork section for povray sources).

`→ Sources <../downloads/pets.tgz>`_

|
|
|

Very outdated
=============

3615 Gen 4 challenge
--------------------

.. image:: ../images/3615_gen4.png
   :class: img-round img-right
   :height: 100px

There was a demo challenge in 1990 for a French Magazine (Génération 4). Here
is my `modest contribution <http://pouet.net/prod.php?which=26985>`_ and a
direct link to the `program <../downloads/wildchip.prg>`_. You'll need an
Atari ST emulator if you want to see it.

|

GFA Punchs
----------

.. image:: ../images/stmag-32.jpg
   :class: img-round img-right
   :height: 160px

There was a challenge in the late eighties to write programs in less than 20
lines of GFA basic. They were published in a French magasine (STMag).

Here is `disk image <../downloads/Punchs.msa>`_ (.msa) with a lot of them. You
can also browse it `online <../downloads/Punchs/>`_.
