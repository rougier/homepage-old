.. include:: ../footer.txt
.. include:: ../header.txt
.. include:: ./sidebar.txt
.. ----------------------------------------------------------------------------

.. .. image:: ../images/WeeMee-Teacher.png
..   :class: img-right

========
Teaching
========

Here is a set of courses on various topics (scientific visualization, neural
networks, computer security and visual attention). Some have been taught at the
national level and consequently they're in French, some others have been taught
at the international level and they're in English. Sources for the slides are
available upon request (by mail).

|

Scientific Visualization
========================

Introduction
------------

.. image:: ../images/ScientificVisualization.png
   :class: img-left img-round
   :height: 140

This lecture was given at Euroscipy 2012, Prace Winter School 2013 and
Euroscipy 2013. It introduces some very basic concepts on scientific
visualization, some good practices and presents a set of open source tools that
may be useful for your own research. This introduction does not require any
pre-requisites. This introduction is generally followed by the matplotlib
tutorial that you will find below.

`→ ScientificVisualization.pdf <../downloads/ScientificVisualization.pdf>`_

|


Matplotlib tutorial
-------------------
.. image:: matplotlib/figures/scatter.png
   :class: img-left img-round
   :height: 140

Matplotlib is probably the single most used Python package for 2D-graphics. It
provides both a very quick way to visualize data from Python and to output
publication-quality figures in many formats. This tutorial proposes to cover
the main aspects of matplotlib through a serie of exerices. This tutorial is
loosely based on the previous `tutorial
<http://scipy-lectures.github.com/intro/matplotlib/matplotlib.html>`_ from the
`scipy lecture notes <http://scipy-lectures.github.com>`_. It has now be
replaced by this one.

`→ Matplotlib tutorial <matplotlib/matplotlib.html>`_

|
|


|

Numerical computing
===================

Numpy beginner tutorial
-----------------------

.. image:: ../images/numpy.png
   :class: img-round img-left
   :height: 140
   :target: numpy/numpy.html

NumPy is the fundamental package for scientific computing with Python.
Besides its obvious scientific uses, NumPy can also be used as an efficient
multi-dimensional container of generic data. Arbitrary data-types can be
defined and this allows NumPy to seamlessly and speedily integrate with a wide
variety of projects.

`→ Numpy tutorial <numpy/numpy.html>`_

|
|


Numpy exercises
---------------

.. image:: ../images/numpy-100.png
   :class: img-left img-round
   :height: 140

Here is a compilation of numpy exercises ranging from neophyte to very advanced
that have been collected from different sources (scipy lecture notes, stack
overflow, numpy user mailing list). The collection is not yet completed but
there are already a decent number of exercices to play with.


`→ 100 Numpy exercises <numpy.100/index.html>`_

|
|



C++ crash course
================

This is an introduction to C++ for C programmers. If you can't understand the
code below, you'd better start with a C tutorial::

    #include <stdio.h>
    void main (int argc, char **argv)
    {
        printf( "Hello World!\n" );
    }

Else, you can follow this `link <c++-crash-course/index.html>`_

|

Reinforcement Learning
======================

This serie of lectures on reinforcement learning was given at the `Third Latin
American Summer School in Computational Neuroscience <http://laconeu.cl>`_,
Valparaiso (Chile) in January 2014.


Part I - Introduction & Definitions
------------------------------------

.. image:: ../images/ReinforcementLearning-1.png
   :class: img-left img-round
   :height: 140

This is an introduction to Markov decision processes (MDP).

`→ ReinforcementLearning-1.pdf <../downloads/ReinforcementLearning-1.pdf>`_

|


Part II - Resolution methods
----------------------------

.. image:: ../images/ReinforcementLearning-2.png
   :class: img-left img-round
   :height: 140

This is an introduction to Reinforcement Learning (RL).

`→ ReinforcementLearning-2.pdf <../downloads/ReinforcementLearning-2.pdf>`_

|
|


Neural Networks
===============

Introduction
------------

.. image:: ../images/LearningAndMemory.png
   :class: img-left img-round
   :height: 140

This is a gentle introduction to learning, memory and artificial neural
networks for master students (in French).

`→ LearningAndMemory.pdf <../downloads/LearningAndMemory.pdf>`_

|
|

Perceptrons
-----------

.. image:: ../images/Perceptron.png
   :class: img-left img-round
   :height: 140

Introduction to perceptron and multi-layer perceptron (in French).

`→ Perceptron.pdf <../downloads/Perceptron.pdf>`_

|
|

Self-Organising maps
--------------------

.. image:: ../images/Kohonen.png
   :class: img-left img-round
   :height: 140

Introduction to self-organising maps and Kohone maps (in French).

`→ Kohonen.pdf <../downloads/Kohonen.pdf>`_

|
|


Computer Security
=================

.. image:: ../images/Security-Overview.png
   :class: img-left img-round
   :height: 140

Depuis les heures glorieuses du "phreaking" où des adolescents cherchaient
simplement à téléphoner gratuitement (1960), jusqu'à la mise au point par des
états de virus informatiques pour des attaques ciblées (2010), le visage de la
cybercriminalité s'est radicalement transformé en l'espace de quelques
années. Là où l'on trouvait des passionés d'informatique, on trouve aujourd'hui
des états, des industries, des mafias et des "script kiddies". Les possibilités
de piratage et de fraude se sont par ailleurs multipliées depuis la
généralisation de l'accès à internet et de la téléphonie mobile. Sachant que le
point d'entrée privilégié dans un système est l'utilisateur lambda, il est plus
que jamais nécessaire de rester vigilant.

| `→ Security-Overview.pdf <../downloads/Security-Overview.pdf>`_
|
|


Visual attention
================

This serie of lectures on visual attention was given at the `NII
<http://www.nii.ac.jp/en/>`_, Tokyo (Japan) in December 2010.


Lecture 1 : Embodied Cognition
------------------------------

.. image:: ../images/Tokyo-2010-Lecture-1.png
   :class: img-left img-round
   :height: 140

Twenty years ago, R. Brooks revealed to the A.I. community that elephants don't
play chess. Ten years later, A. Clark explained that *we ignore the fact that
the biological mind is, first and foremost, an organ for controlling the
biological body. Minds make motions, and they must make them fast - before the
predator catches you, or before your prey gets away from you.  Minds are not
disembodied logical reasoning devices.* This lecture proposes to look back at
(almost) 60 years of Artificial Intelligence researches in order to address the
question of what has been accomplished so far towards our understanding of
intelligence and cognition. In this context, we'll introduce the
action-perception loop, the embodied cognition paradigm and the symbol
grounding problem as it has been identified by Steve Harnad. This problem has
became prominent in the cognitive science society and the idea that a symbol is
much more than a mere meaningless token that can be processed through some
algorithm sheds a new light on higher brain functions. More specifically, we'll
explain how those theories can impact modeling on computer vision.

| `→ Lecture-1.pdf <../downloads/Tokyo-2010-Lecture-1.pdf>`_
| `→ Lecture-1.pdf (printer friendly) <../downloads/Tokyo-2010-Lecture-1-white.pdf>`_
|


Lecture 2: Visual Attention
---------------------------

.. image:: ../images/Tokyo-2010-Lecture-2.png
   :class: img-left img-round
   :height: 140

This lecture proposes to review current psychological and physiological data as
and classical experiments related to visual attention as well as anatomical and
physiological data related to the oculomotor control in the primate. We will
introduce the two main forms of visual attention, namely exogeneous (bottom up)
and endogeneous (top down) visual attention that are known to play a critical
role in the perception and processing of a visual scene.  Facilitating and
inhibitory effects of visual attention will be presented in light of Posner
experiments (1980) related to the concept of inhibition of return that play a
major role in a number of computational models of visual attention. Finally,
integrative theories related to visual attention will be introduced, namely the
premotor theory of attention, the active perception paradigm and the deictic
codes for the embodiment of cognition.

| `→ Lecture-2.pdf <../downloads/Tokyo-2010-Lecture-2.pdf>`_
| `→ Lecture-2.pdf (printer friendly) <../downloads/Tokyo-2010-Lecture-2-white.pdf>`_
|


Lecture 3: Dynamic Neural Fields
--------------------------------

.. image:: ../images/Tokyo-2010-Lecture-3.png
   :class: img-left img-round
   :height: 140

This lecture introduces main concepts related to classical artificial neural
networks as well as computational neuroscience.  Standard artificial neural
network models related to supervised, unsupervised and reinforcment learning
will be briefly introduced as well as key concepts from neuro-anatomy and
neuro-physiology.  This lecture will also focus on the dynamic neural field
(DNF) Theory as it has been originally introduced by Wilson and Cowan in the
early seventies and later formalized by S.I.  Amari and J.G. Taylor.  These
theories explain the dynamic of pattern formation for lateral-inhibition type
homogeneous neural fields with general connections. They show that, in some
conditions, continuous attractor neural networks are able to maintain a
localised bubble of activity in direct relation with the excitation provided by
a stimulation.  We will investigate further these theories in order to explain
how their functional properties can be linked to visual attention defined as
the capacity to attend to one stimulus in spite of noise, distractors or
saliency effects.

| `→ Lecture-3.pdf <../downloads/Tokyo-2010-Lecture-3.pdf>`_
| `→ Lecture-3.pdf (printer friendly) <../downloads/Tokyo-2010-Lecture-3-white.pdf>`_
|


Lecture 4: Models of Visual Attention
-------------------------------------------------------------------------------

.. image:: ../images/Tokyo-2010-Lecture-4.png
   :class: img-left img-round
   :height: 140

The visual exploration of a scene involves the interplay of several competing
processes (for example to select the next saccade or to keep fixation) and the
integration of bottom-up (e.g. contrast) and top-down information (the target
of a visual search task). Identifying the neural mechanisms involved in these
processes and the integration of these information remain a challenging
question. Visual attention refers to all these processes, both when the eyes
remain fixed (covert attention) and when they are moving (overt attention).
Popular computation models of visual attention consider that the visual
information remains fixed when attention is deployed while the primate are
executing around three saccadic eye movements per second, abruplty changing the
whole visual information.  We'll introduce in this lecture a model relying on
dynamic neural fields and show that covert and overt attention can emerge from
such a substratum.  We'll identify and propose a possible interaction of four
elementary mechanisms for selecting the next locus of attention, memorizing the
previously attended locations, anticipating the consequences of eye movements
and integrating bottom-up and top-down information in order to perform a visual
search task with saccadic eye movements.

| `→ Lecture-4.pdf <../downloads/Tokyo-2010-Lecture-4.pdf>`_
| `→ Lecture-4.pdf (printer friendly) <../downloads/Tokyo-2010-Lecture-4-white.pdf>`_
|
