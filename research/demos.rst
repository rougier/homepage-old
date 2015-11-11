.. include:: ../footer.txt
.. include:: ../header.txt
.. include:: ./sidebar.txt
.. ----------------------------------------------------------------------------

=====
Demos
=====

Here is set of demonstrations that are linked to some researches. Click on a
picture to see the corresponding movie. All the sources are available from this
page or from the `coding <../coding/index.html>`_ page.

|

Emergence of attention within a neural population
=================================================

* **N.P. Rougier and J. Vitay** « *Emergence of Attention within a Neural
  Population* », Neural Networks, volume 19, number 5, pages 573—581, 2006.

We present a dynamic model of attention based on the Continuum Neural Field
Theory that explains attention as being an emergent property of a neural
population. This model is experimentally proved to be very robust and able to
track one static or moving target in the presence of very strong noise or in
the presence of a lot of distractors, even more salient than the target. This
attentional property is not restricted to the visual case and can be considered
as a generic attentional process of any spatio-temporal continuous input.


.. image:: ../images/attention-noise.png
   :class: img-polaroid
   :width: 30%
   :target: ../movies/noise-high.mp4

.. image:: ../images/attention-distractors.png
   :class: img-polaroid
   :width: 30%
   :target: ../movies/distractors-high.mp4

.. image:: ../images/attention-saliency.png
   :class: img-polaroid
   :width: 30%
   :target: ../movies/saliency-high.mp4

|

**Sources**

* | `attention-noise.py <../downloads/attention-noise.py>`_
* | `attention-distractors.py <../downloads/attention-distractors.py>`_
* | `attention-saliency.py <../downloads/attention-saliency.py>`_

|


A distributed model of visual spatial attention
===============================================

* **J. Vitay, N.P. Rougier and F. Alexandre**, « *A distributed model
  of visual spatial attention* », Biomimetic neural learning for intelligent
  robots : intelligent systems, cognitive robotics, and neuroscience, 2005,
  Volume 3575, pages 54—72.

Although biomimetic autonomous robotics relies on the massively parallel
architecture of the brain, the key issue is to temporally organize
behaviour. The distributed representation of the sensory information has to be
coherently processed to generate relevant actions. In the visual domain, we
propose here a model of visual exploration of a scene by the means of localized
computations in neural populations whose architecture allows the emergence of a
coherent behaviour of sequential scanning of salient stimuli. It has been
implemented on a real robotic platform exploring a moving and noisy scene
including several identical targets.

.. image:: ../images/INRIA.jpg
   :class: img-polaroid
   :width: 30%
   :target: ../movies/INRIA.mp4

.. image:: ../images/lemmons.jpg
   :class: img-polaroid
   :width: 44%
   :target: ../movies/lemmons.mp4

|

**Sources**

`→ dana website <http://dana.loria.fr>`_

|

Spatial memory anticipation during visual search
================================================

* **J. Fix, J. Vitay and N.P. Rougier**, « *A Computational Model of Spatial
  Memory Anticipation during Visual Search* », Anticipatory Behavior in
  Adaptive Learning Systems: From Brains to Individual and Social Behavior
  Springer-Verlag Berlin Heidelberg (Ed.) (2007).

Some visual search tasks require to memorize the location of stimuli that have
been previously scanned. Considerations about the eye movements raise the
question of how we are able to maintain a coherent memory, despite the frequent
drastically changes in the perception. In this article, we present a
computational model that is able to anticipate the consequences of the eye
movements on the visual perception in order to update a spatial memory.

.. image:: ../images/saccades-1.png
   :class: img-polaroid
   :width: 30%
   :target: ../movies/video1.avi

.. image:: ../images/saccades-2.png
   :class: img-polaroid
   :width: 30%
   :target: ../movies/video2.avi

.. image:: ../images/saccades-5.png
   :class: img-polaroid
   :width: 30%
   :target: ../movies/video5.avi

|

**Sources**

`→ dana website <http://dana.loria.fr>`_

|

Dynamic Self-Organizing maps
============================

* **N.P.Rougier and Y.Boniface**, « *Dynamic Self-Organising map* »,
  Neurocomputing 74, 11, (2011), 1840—1847.

We present a variation of the self-organising map algorithm where the original
time-dependent (learning rate and neighbourhood) learning function is replaced
by a time-invariant one. This allows for on-line and continuous learning on
both static and dynamic data distributions. One of the property of the newly
proposed algorithm is that it does not fit the magnification law and the
achieved vector density is not directly proportional to the density of the
distribution as found in most vector quantisation algorithms. From a biological
point of view, this algorithm sheds light on cortical plasticity seen as a
dynamic and tight coupling between the environment and the model.


.. image:: ../images/DSOM-sphere.png
   :class: img-polaroid
   :width: 30%
   :target: ../movies/DSOM-sphere.mp4

.. image:: ../images/DSOM-cube.png
   :class: img-polaroid
   :width: 30%
   :target: ../movies/DSOM-cube.mp4

.. image:: ../images/DSOM-sphere-cube.png
   :class: img-polaroid
   :width: 30%
   :target: ../movies/DSOM-sphere-cube.mp4

|

**Sources**

`→ dynamic-som.tgz <../downloads/dynamic-som.tgz>`_

|

A Neural Field Model of the Somatosensory Cortex
================================================

* **G.Is. Detorakis, N.P. Rougier**, « *A Neural Field Model of the
  Somatosensory Cortex: Formation, Maintenance and Reorganization of Ordered
  Topographic Maps* », Plos ONE 7(7), 2012.


We investigate the formation and maintenance of ordered topographic maps in the
primary somatosensory cortex as well as the reorganization of representations
after sensory deprivation or cortical lesion. We consider both the critical
period (postnatal) where representations are shaped and the post-critical
period where representations are maintained and possibly reorganized. We
hypothesize that feed-forward thalamocortical connections are an adequate site
of plasticity while cortico-cortical connections are believed to drive a
competitive mechanism that is critical for learning. We model a small skin
patch located on the distal phalangeal surface of a digit as a set of 256
Merkel ending complexes (MEC) that feed a computational model of the primary
somatosensory cortex (area 3b). This model is a two-dimensional neural field
where spatially localized solutions (a.k.a. bumps) drive cortical plasticity
through a Hebbian-like learning rule. Simulations explain the initial formation
of ordered representations following repetitive and random
\highlightII{stimulations} of the skin patch. Skin lesions as well as cortical
lesions are also studied and results confirm the possibility to reorganize
representations using the same learning rule and depending on the type of the
lesion. For severe lesions, the model suggests that cortico-cortical
connections may play an important role in complete recovery.


.. image:: ../images/DNF-SOM.jpg
   :class: img-polaroid
   :width: 30%
   :target: ../movies/DNF-SOM.mp4

.. image:: ../images/DNF-SOM-RF.jpg
   :class: img-polaroid
   :width: 30%
   :target: ../movies/DNF-SOM-RF.mp4

.. image:: ../images/DNF-SOM-25RFs.jpg
   :class: img-polaroid
   :width: 30%
   :target: ../movies/DNF-SOM-25RFs.mp4

|

**Sources**
`→ plos_one.tgz <../downloads/plos_one.tgz>`_
