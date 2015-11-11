.. default-role:: math
.. header:: **N.P. Rougier & Y. Boniface** | Dynamic Self-Organising Map

===============================================================================
Dynamic Self-Organising Map                                                    
===============================================================================

-------------------------------------------------------------------------------
A computational model of cortical plasticity                                   
-------------------------------------------------------------------------------

**Nicolas P. Rougier** ¹ and **Yann Boniface** ²

| **¹** LORIA/INRIA Nancy - Nicolas.Rougier@inria.fr
| **²** LORIA/Université Nancy 2 - Yann.Boniface@inria.fr

.. contents:: Table of Contents
   :depth: 2

.. sectnum::
   :suffix: .
   :depth:  3

.. abstract::

   We present  in this paper a  variation of the  self-organising map algorithm
   where the original time-dependent (learning rate and neighbourhood) learning
   function is  replaced by a time-invariant  one. This allows  for on-line and
   continuous learning  on both static  and dynamic data distributions.  One of
   the property  of the newly  proposed algorithm is  that it does not  fit the
   magnification  law   and  the  achieved  vector  density   is  not  directly
   proportional  to the density  of the  distribution as  found in  most vector
   quantisation algorithms.   From a biological  point of view,  this algorithm
   sheds  light on cortical  plasticity seen  as a  dynamic and  tight coupling
   between the environment and the model.

.. keywords::

   SOM, self organisation, cortical plasticity, dynamic.



Introduction                                                                   
===============================================================================

Vector  quantisation (VQ)  refers to  the  modelling of  a probability  density
function  into  a discrete  set  of  prototype  vectors (sometimes  called  the
codebook) such  that any  point drawn from  the associated distribution  can be
associated to a  prototype vector. Most VQ algorithms try  to match the density
through the density of their codebook: high density regions of the distribution
tend to have more associated prototypes than low density region. This generally
allows to minimise  the loss of information (or distortion)  as measured by the
mean quadratic error. For a complete picture, it is to be noted that there also
exists some  cases where  only a partition  of the  space occupied by  the data
(regardless of their density) is necessary.  In this case, one wants to achieve
a regular  quantification *a priori*  of the probability density  function. For
example, in some classification problems, one wants to achieve a discrimination
of data in term  of classes and thus needs only to  draw frontiers between data
regardless of their respective density.

Vector quantisation can be achieved using several methods such as variations of
the   k-means   method   [MacQueen:1967]_,  Linde-Buzo-Gray   (LBG)   algorithm
[Linde+Al:1980]_ or neural network models such as the self-organising map (SOM)
[Kohonen:1982]_, neural  gas (NG)  [Martinetz+Al:1993]_ and growing  neural gas
(GNG) [Fritzke:1995]_. Among all these  methods, the SOM algorithm is certainly
the most famous in the field  of computational neuroscience since it can give a
biologically and plausible  account on the organisation of  receptive fields in
sensory  areas  where adjacent  neurons  shares  similar representations.   The
stability  and the  quality  of  such self-organisation  depends  heavily on  a
decreasing learning rate as well  as a decreasing neighbourhood function.  This
is quite  congruent with the idea  of a critical  period in the early  years of
development where most sensory or  motor properties are acquired and stabilised
[Hubel+Wiesel:1965]_,  [Hubel+Wiesel:1970]_, [Daw:1994]_.  However,  this fails
to explain cortical  plasticity since we know that the  cortex has the capacity
to  re-organise itself  in face  of lesions  or  deficits [BachyRita+Al:1969]_,
[BachyRita:1972]_,  [Ramachadran+Al:1992]_.  The  question is  then to  know to
what extent  it is possible to  have both stable and  dynamic representations ?
We propose to answer this question  by considering a tight coupling between the
environment  and  cortical  representations.   If the  environment  is  stable,
cortical representations  should remain stable and if  the environment suddenly
changes,  cortical  representations   must  dynamically  adapt  themselves  and
stabilise  again onto  the new  environment.

Quite obviously, this cannot be achieved using SOM-like algorithms that depends
on a time decreasing learning rate and/or neighbourhood function (SOM, NG, GNG)
and,  despite the  huge  amount of  literature [Oja+Al:2003]_  [Kaski+Al:1998]_
around self-organising  maps and Kohonen-typed  networks (more than  7000 works
listed in  [Pöllä+Al:2009]_), there is  is surprisingly and  comparatively very
little  work dealing  with online  learning  (also referred  as incremental  or
lifelong learning). Furthermore,  most of these works are  based on incremental
models, that  is, networks  that create and/or  delete nodes as  necessary. For
example,   the  modified   GNG  model   [Fritzke:1997]_  is   able   to  follow
non-stationary  distributions by  creating  nodes  like in  a  regular GNG  and
deleting them when  they have a too small  *utility* parameter.  Similarly, the
evolving self-organising  map (ESOM, [Deng+Al:2000]_,  [Deng+Al:2003]_ is based
on an incremental  network quite similar to GNG  that creates dynamically based
on the measure of  the distance of the winner to the data  (but the new node is
created  at   exact  data   point  instead  of   the  mid-point  as   in  GNG).
Self-organising  incremental neural  network (SOINN)  [Furao+Al:2006]_  and its
enhanced  version (ESOINN) [Furao+Al:2007]_  are also  based on  an incremental
structure  where the  first version  is using  a two  layers network  while the
enhanced version proposed a single  layer network. One noticeable result is the
model  proposed by  [Keith-Magee:2001]_ which  does not  rely on  a incremental
structure but  is based  on the  Butterworth decay scheme  that does  not decay
parameters  to  zero.   The  model  works  in  two  phases,  an  initial  phase
(approximately ten epochs) is used  to establish a rough global topology thanks
to a very  large neighbourhood and the second phase  uses a small neighbourhood
phase to train the network. Unfortunately, the size of the neighbourhood in the
second phase has to be adapted to the expected density of the data.

Without  judging performances  of these  models, we  do not  think they  give a
satisfactory answer to our initial question and we propose instead to answer by
considering a  tight coupling between  the environment and  representations. If
the  environment is  stable, representations  should remain  stable and  if the
environment suddenly changes, representations must dynamically adapt themselves
and stabilise  again onto the new  environment.  We thus  modified the original
SOM algorithm in order to  make its learning rule and neighbourhood independent
of time. This results in a tight coupling between the environment and the model
that  ensure  both stability  and  plasticity.  In  next section,  we  formally
describe the dynamic self-organising map  in the context of vector quantisation
and both neural gas and self-organising  map are formally described in order to
underline  differences   between  the   three  algorithms.  The   next  section
re-introduces  the  model  from a  more  behavioural  point  of view  and  main
experimental results are  introduced using either low or  high dimensional data
and offers  side-to-side comparison  with other algorithms.  Results concerning
dynamic   distributions  are   also   introduced  in   the   case  of   dynamic
self-organising  map   in  order  to   illustrate  the  coupling   between  the
distribution and the  model. Finally, we discuss the relevancy  of such a model
in the context of computational neurosciences and embodied cognition.



Definitions                                                                    
===============================================================================
Let us  consider a  probability density function  `f(x)` on a  compact manifold
`\Omega \in \mathbb{R}^d`. A vector quantisation (VQ) is a function `\Phi` from
`\Omega`  to   a  finite   subset  of  `n`   code  words   `\{\mathbf{w}_i  \in
\mathbb{R}^d\}_{1 \leq i \leq n}` that  form the codebook. A cluster is defined
as  `C_i \deq  \{x  \in \Omega  | \Phi(x)  =  \mathbf{w}_i \}`,  which forms  a
partition of  `\Omega` and  the distortion of  the VQ  is measured by  the mean
quadratic error

.. math::

   \xi = \sum_{i=1}^{n} \int_{C_i} \lVert x - \mathbf{w}_i \rVert^2 f(x) dx.

If the  function `f` is unknown  and a finite  set `\{x_i\}` of `p`  non biased
observations is available, the distortion error may be empirically estimated by

.. math::
  :label: error

  \hat{\xi} = \frac{1}{p}\sum_{i=1}^{n} \sum_{x_j \in C_i} \lVert
  x_j-\mathbf{w}_i \rVert^2.

Neural  maps define  a special  type of  vector quantifiers  whose  most common
approaches   are   the   Self-Organising    Map   (SOM),   Elastic   Net   (EN)
[Durbin+Willshaw:1987]_, Neural Gas (NG) and  Growing Neural Gas (GNG).  In the
following,   we   will   use    definitions   and   notations   introduced   by
[Villman+Clausen:2006]_ where a neural map  is defined as the projection from a
manifold  `\Omega  \subset  \mathbb{R}^d`  onto  a  set  `\mathcal{N}`  of  `n`
*neurons* which is formally written as `\Phi : \Omega \rightarrow \mathcal{N}`.
Each neuron `i` is associated with a code word `\mathbf{w}_i \in \mathbb{R}^d`,
all of which established the set `\{\mathbf{w}_i\}_{i \in \mathcal{N}}` that is
referred  as the  codebook. The  mapping from  `\Omega` to  `\mathcal{N}`  is a
closest-neighbour  winner-take-all rule  such that  any vector  `\mathbf{v} \in
\Omega` is mapped  to a neuron `i` with  the code `\mathbf{w}_\mathbf{v}` being
closest to the actual presented stimulus vector `\mathbf{v}`,

.. math::
   :label: psi

   \Phi : \mathbf{v} \mapsto \argmin_{i \in \mathcal{N}} (\lVert \mathbf{v} -
   \mathbf{w}_i \rVert).

The neuron `\mathbf{w}_\mathbf{v}` is called  the *winning element* and the set
`C_i =  \{x \in \Omega  | \Phi(x) =  \mathbf{w}_i \}` is called  the *receptive
field* of the neuron `i`. The  geometry corresponds to a Voronoï diagram of the
space with `\mathbf{w}_i` as the center.


Self-Organising Maps (SOM)                                                     
-------------------------------------------------------------------------------
SOM is a neural map equipped with a structure (usually a hypercube or hexagonal
lattice) and each element `i`  is assigned a fixed position `\mathbf{p}_{i}` in
`\mathbb{R}^q`  where `q`  is  the dimension  of  the lattice  (usually `1`  or
`2`). The learning process is an  iterative process between time `t=0` and time
`t=t_f \in \mathbb{N}^+` where vectors `\mathbf{v} \in \Omega` are sequentially
presented to the map with respect  to the probability density function `f`. For
each presented vector `\mathbf{v}` at time `t`, a winner `s \in \mathcal{N}` is
determined according to equation  :eq:`psi`.  All codes `\mathbf{w}_{i}` from
the codebook are shifted towards `\mathbf{v}` according to

.. math::
   :label: som-learning

   \Delta\mathbf{w}_{i} = \varepsilon(t)~h_\sigma(t,i,s)~(\mathbf{v} -
   \mathbf{w}_i)

with `h_\sigma(t,i,j)` being a neighbourhood function of the form

.. math::
   :label: som-neighborhood

   h_\sigma(t,i,j) = e^{- \frac{\lVert \mathbf{p}_i - \mathbf{p}_j
   \rVert^2}{2\sigma(t)^2}}.

where `\varepsilon(t) \in \mathbb{R}` is the learning rate and `\sigma(t) \in
\mathbb{R}` is the width of the neighbourhood defined as

.. math::

  \sigma(t) = \sigma_i\left(\frac{\sigma_f}{\sigma_i}\right)^{t/t_f}, \text{
  with } \varepsilon(t) =
  \varepsilon_i\left(\frac{\varepsilon_f}{\varepsilon_i}\right)^{t/t_f},

while  `\sigma_i`  and  `\sigma_f`  are  respectively  the  initial  and  final
neighbourhood  width and `\varepsilon_i`  and `\varepsilon_f`  are respectively
the initial  and final learning rate.  We usually have  `\sigma_f \ll \sigma_i`
and `\varepsilon_f \ll \varepsilon_i`.


Neural Gas (NG)                                                                
-------------------------------------------------------------------------------
In the  case of NG, the learning  process is an iterative  process between time
`t=0` and time  `t=t_f \in \mathbb{N}^+` where vectors  `\mathbf{v} \in \Omega`
are sequentially presented  to the map with respect  to the probability density
function `f`. For  each presented vector `\mathbf{v}` at  time `t`, neurons are
ordered  according  to  their  respective  distance  to  `\mathbf{v}`  (closest
distances map to lower ranks)  and assigned a rank `k_i(\mathbf{v})`. All codes
`\mathbf{w}_{i}` from  the codebook are shifted  towards `\mathbf{v}` according
to

.. math::
   :label: ng-learning

   \Delta\mathbf{w}_{i} = \varepsilon(t)~h_\lambda(t,i,\mathbf{v})~(\mathbf{v} -
   \mathbf{w}_i)

with `h_\lambda(t,i,\mathbf{v})` being a neighbourhood function of the form:

.. math::
   :label: ng-neighborhood

   h_{\lambda}(t,i,\mathbf{v}) = e^{-\frac{k_i(\mathbf{v})}{\lambda(t)}}

where `\varepsilon(t) \in \mathbb{R}` is the learning rate and `\lambda(t) \in
\mathbb{R}` is the width of the neighbourhood defined as

.. math::

  \lambda(t) = \lambda_i\left(\frac{\lambda_f}{\lambda_i}\right)^{t/t_f},
  \text{ with }
  \varepsilon(t) =
  \varepsilon_i\left(\frac{\varepsilon_f}{\varepsilon_i}\right)^{t/t_f},

while  `\lambda_i`  and `\lambda_f`  are  respectively  the  initial and  final
neighbourhood  and  `\varepsilon_i` and  `\varepsilon_f`  are respectively  the
initial and final learning rate.  We usually have `\lambda_f \ll \lambda_i` and
`\varepsilon_f \ll \varepsilon_i`.


Dynamic Self-Organising Map (DSOM)                                             
-------------------------------------------------------------------------------
DSOM  is a  neural map  equipped  with a  structure (a  hypercube or  hexagonal
lattice) and each  neuron `i` is assigned a  fixed position `\mathbf{p}_{i}` in
`\mathbb{R}^q`  where `q`  is  the dimension  of  the lattice  (usually `1`  or
`2`). The  learning process is  an iterative process where  vectors `\mathbf{v}
\in  \Omega`  are  sequentially  presented  to  the map  with  respect  to  the
probability density  function `f`.  For  each presented vector  `\mathbf{v}`, a
winner `s \in  \mathcal{N}` is determined according to  equation :eq:`psi`. All
codes  `\mathbf{w}_{i}`  from the  codebook  `\mathbf{W}`  are shifted  towards
`\mathbf{v}` according to

.. math::
   :label: dsom-learning

   \Delta\mathbf{w}_{i} = \varepsilon \lVert \mathbf{v} -
   \mathbf{w}_i\rVert_\Omega~h_\eta(i,s,\mathbf{v})~(\mathbf{v} - \mathbf{w}_i)

withj `\varepsilon` being a constant learning rate and `h_\eta(i,s,\mathbf{v})`
being a neighbourhood function of the form

.. math::
   :label: dsom-neighborhood

   h_\eta(i,s,\mathbf{v}) =
      e^{-\frac{1}{\eta^2} \frac{\lVert \mathbf{p}_i - \mathbf{p}_s
          \rVert^2}{{\lVert \mathbf{v} - \mathbf{w}_s \rVert}_{\Omega}^{2}}}

where `\eta`  is the *elasticity*  or *plasticity* parameter. If  `\mathbf{v} =
\mathbf{w}_s`, then `h_\eta(i,s,\mathbf{v}) = 0`.


Model                                                                          
===============================================================================
As  we explained  in  the introduction,  the  DSOM algorithm  is essentially  a
variation  of the SOM  algorithm where  the time  dependency has  been removed.
Regular  learning   function  :eq:`som-learning`  and   neighbourhood  function
:eq:`som-neighborhood`   have   been   respectively   replaced   by   equations
:eq:`dsom-learning` and :eq:`dsom-neighborhood` which reflect two main ideas:

- If a neuron is close enough to the data, there is no need for others to
  learn anything: the winner can represent the data.
- If there is no neuron close enough to the data, any neuron learns
  the data according to its own distance to the data.

This  draws several consequences  on the  notion of  neighbourhood that  is now
dynamic and  leads to a  qualitatively different self-organisation that  can be
controlled using a free elasticity parameter.


Dynamic neighbourhood                                                          
-------------------------------------------------------------------------------
Learning rate is  modulated using the closeness of the winner  to the data. The
figure  :fig:`learning-rate`  represents this  learning  rate  modulation as  a
function of a data `\mathbf{v}`, a  neuron `i` (with code `\mathbf{w}_i`) and a
winner `s` (with code `\mathbf{w}_s`). If the winner `s` is very close or equal
to  `\mathbf{v}` (bottom  line  on the  figure),  learning rate  of any  neuron
different from the  winner `s` is zero and only the  winner actually learns the
new data. When the winner `s` is  very far from the data (top line), any neuron
benefits from a large learning rate and learns the new data (modulated by their
own distance  to the data but this  extra modulation is not  represented on the
figure).

.. figure::   images/learning-rate.png
   :target:   images/learning-rate.png
   :width:    75%
   :label:    learning-rate

   At each presented data `\mathbf{v}`, the learning rate of each neuron `i` is
   modulated according  to both the distance `\lVert  \mathbf{w}_s - \mathbf{v}
   \rVert`  (which represents  the  distance  between the  winner  `s` and  the
   presented  data  `\mathbf{v}`)  and  the  distance  `\lVert  \mathbf{p}_i  -
   \mathbf{p}_s  \rVert` (which represent  the distance  between code  words of
   neuron `i`  and neuron `s`).  If  the winner `s`  is very close or  equal to
   `\mathbf{v}`  (bottom line  on  the  figure), learning  rate  of any  neuron
   different from  the winner `s` is  zero and only the  winner actually learns
   the new data. When the winner `s`  is very far from the data (top line), any
   neuron  benefits  from  a  large  learning  rate and  learns  the  new  data
   (modulated by  their own distance to  the data but this  extra modulation is
   not represented on the figure).



This notion  of closeness of the  winner to the  data is thus critical  for the
algorithm and  modifies considerably both  the notion of neighbourhood  and the
final codebook.  Most  VQ tries to capture data density  through the density of
their codebook as introduced in [Villman+Clausen:2006]_ where authors considers
the generalised error

.. math::

   E_\gamma = \int_\Omega \lVert \mathbf{w}_s - \mathbf{v} \rVert^\gamma
  P(\mathbf{v}) d\mathbf{v}

and  introduces the  relation  `P(\mathbf{w}) \propto  \rho(\mathbf{w})^\alpha`
with `\rho(\mathbf{w})` being the weight  vector density and `\alpha` being the
*magnification  exponent*  or  *magnification   factor*.  If  we  consider  the
intrinsic  (or Hausdorff)  dimension  `d`  of the  data,  the relation  between
magnification and `d` is given by `\alpha = \frac{d}{d+\gamma}` and an ideal VQ
achieves a  magnification factor of  1. However, DSOM algorithm  clearly states
that if a neuron is already close  enough to a presented data, there is no need
for the neighbours  to learn anything and this results in  a codebook that does
not follow the magnification law as illustrated on figure :fig:`density` for
three very simple two-dimensional non homogeneous distributions.

.. figure:: images/density.png
   :target: images/density.png
   :label:  density
   
   Three DSOM have been trained  on a disc distribution using different density
   areas.   **Left.**   The   density    is   uniform   all   over   the   disc
   (0.25).  **Center**. Outer  ring has  higher  density (.4)  than inner  disc
   (.1).  **Right**.  Outer  ring  has  lower  density  (.1)  than  inner  disc
   (.4).  Despite  these  different   density  distributions,  the  three  DSOM
   self-organise onto the support of the distribution (the whole disc) and does
   not try to match density.

Said differently,  what is actually  mapped by the  DSOM is the  *structure* or
*support* of  the distribution (`\Omega` using notations  introduced in section
[definitions]_) rather than the density.


Elasticity                                                                     
-------------------------------------------------------------------------------
The DSOM algorithm is not parameter free since we need to control when a neuron
may be considered to be *close enough* to a data such that it prevents learning
for its neighbours. This is the role of the elasticity parameter that modulates
the   strength  of   the  coupling   between   neurons  as   shown  on   figure
:fig:`elasticity` for a simple two-dimensional normal distribution.

.. figure:: images/elasticity.png
   :target: images/elasticity.png
   :label:  elasticity

   Three DSOM with respective elasticity equal  to 1, 2 and 3 have been trained
   for 20 000 iterations on a normal distribution using a regular grid covering
   the  `[0,1]^2` segment  as  initialisation. Low  elasticity  leads to  loose
   coupling between neurons while higher elasticity results in a tight coupling
   between neurons.

This  notion  of elasticity  shares  some  common  concepts with  the  Adaptive
Resonance Theory (ART)  as it has been introduced  in [Grossberg:1987]_. In the
ART model, the  vigilance parameter has a critical  influence on learning since
it  controls the  actual partition  of the  input space:  high  vigilance level
produces  high  number of  very  precise  memories  while low  vigilance  level
produces  fewer  and  more generic  memories.   This  is  very similar  to  the
elasticity parameter:  if elasticity is  high, neurons tend to  pack themselves
very  tightly  together (code  vectors  are  relatively  close) while  a  lower
elasticity allows for looser coupling  between neurons. However, in the case of
ART, the vigilance parameter also  governs the number of final prototypes since
they can be  created on demand. In  the case of DSOM, the  number of prototypes
(i.e. neurons) is fixed and they are  supposed to span the whole input space to
ensure convergence. Consequently, there  exists a relation between the diameter
of  the support  (defined as  the maximum  distance between  any two  points in
`\Omega`), the number of neurons and the elasticity parameter. In the one hand,
if elasticity  is too high,  neurons cannot span  the whole space and  the DSOM
algorithm  does not  converge, in  the other  hand, if  elasticity is  too low,
coupling between  neurons is weak  and may prevent self-organisation  to occur:
code-vectors  are evenly  spread on  the support  but they  do not  respect the
neighbourhood   relationship  anymore.  There   certainly  exists   an  optimal
elasticity for a  given distribution but we did not  yet investigate fully this
relationship and we do not have  formal results. As a preliminary work, we have
studied the relationship  between elasticity and the initial  conditions in the
one dimensional case  using a very simple experimental  setup where the dataset
is made  of only  two samples (one  at 0 and  the other  at 1) as  explained on
figure  :fig:`convergence`. This figure  clearly shows  a discontinuity  in the
error when  elasticity is varying from 1.0  to 4.0 but at  different places for
different  initial conditions.  The reason  comes  from the  dependency of  the
learning to the  distance between the winner node and  the presented data. When
this difference is  large, a large correction of weights  occur on all networks
nodes  and this is  only attenuated  by their  distance to  the winner  and the
network elasticity.

.. figure:: images/convergence.png
   :target: images/convergence.png
   :label:  convergence

   Several  one-dimensional DSOM  with two  nodes  have been  trained for  2500
   epochs  using  a dataset  of  two  samples (0  and  1)  that were  presented
   alternatively. Each  point of each curve  represents the error  of a network
   with  given elasticity  and initial  conditions. Point  A represents  a case
   where elasticity is too high and  makes the network to oscillate while point
   B represents a case where elasticity  was low enough to allow the network to
   properly converge (towards x=0 and y=1).

In  the   presented  experimental  setup,   data  (0  and  1)   were  presented
alternatively and lead  to a convergence when elasticity was  low enough and to
an oscillatory  behaviour (not visible on  the figure) when  elasticity was too
high. This oscillatory behaviour can  be understood most simply when looking at
scheme A  on the  figure. Each  correction made to  the network  in one  way is
immediately  counter-balanced in  the other  way when  next data  is presented.
This  preliminary  study  lead us  to  think  that  the  choice of  an  optimal
elasticity not  only depends on  the size  of the network  and the size  of the
support but also  on the initial conditions. If we were  to generalise from the
simple study above,  the initial configuration of the  network should cover the
entire support as much as possible to reduce elasticity dependency.


Convergence                                                                    
-------------------------------------------------------------------------------
It  is well known  that the  convergence of  the Kohonen  algorithm has  not be
proved  in the  general case  [Cottrel+Al:1998]_ even  though  some conditional
convergence  properties  have  been  established in  the  one-dimensional  case
[Cottrell+Al:1987]_. Furthermore, in the case  of continuous input, it has been
shown that there does not  exist an associated energy function [Erwin+Al:1992]_
and in the  case of a finite  set of training patterns, the  energy function is
highly discontinuous [Heskes:1999]_. In the  case of the dynamic SOM, the proof
of convergence is straightforward since we  can exhibit at least one case where
the DSOM does not converge, when the number of nodes is less then the number of
data as illustrated on figure :fig:`wrong`.

.. figure:: images/wrong.png
   :target: images/wrong.png
   :label:  wrong

   Due to its  dynamic nature, the dynamic SOM cannot  converge when the number
   of nodes (4 here)  is less than the number of data (5  here). NG and SOM can
   converge on an approximated solution  thanks to both their decaying learning
   rate and neighborhood and this  explains why three nodes are exactly aligned
   with  their corresponding  data while  the  last node  found a  mid-distance
   position. In  the case of  DSOM and because  of the constant  learning rate,
   every node is moving at each presented data and thus cannot converge at all.

Most generally, in case where the number of nodes is less than the total number
of   presented  data,  we   can  predict   that  the   dynamic  SOM   will  not
converge. Moreover, a similar problem occurs  if the number of nodes is exactly
equal to the number of data  and if nodes are initially distributed uniquely on
each data.  In such an  initial setup, the  learning parameter is zero  for any
presented data and this prevents the network to learn anything at all. We could
say that it does converge in such a case (network is frozen) but if the initial
configuration does  not correspond to a  proper unfolded one,  the answer would
not  be really  satisfactory.  A proof  of  convergence would  then require  to
identify configurations  (initial conditions, size,  elasticity, learning rate)
where the network  may have chances to converge but we  think this is currently
out of the scope of this paper.



Experimental results                                                           
===============================================================================
We report  in this section some  experimental results we  obtained on different
types of distribution that aim at  illustrating DSOM principles. We do not have
yet  formal results  about convergence  and/or quality  of the  codebook.  As a
consequence, these results do not  pretend to prove anything and are introduced
mainly to illustrate qualitative behaviour of the algorithm.

Unless stated otherwise, the learning procedure in following examples is:

- A distribution is chosen (normal, uniform, etc.)
- A discrete sample set of samples is drawn from the distribution
- Model learns for `n` iterations
- At each iteration, a sample is picked randomly and uniformly in the
  discrete sample set
- Distortion is measured on whole sample set every 100 iterations using
  equation :eq:`error`. 

The  distortion  error  is  plotted   above  each  graphics  to  show  rate  of
convergence.


Non stationary distribution                                                    
-------------------------------------------------------------------------------
In order  to study dynamic  aspect of the  DSOM algorithm, three  networks (NG,
SOM, DSOM)  have been trained for  20 000 iterations on  a dynamic distribution
that vary  along time: a  uniform distribution (1) on  [0.0,0.5]×[0.0,0.5] from
iterations 0  to 5000, a  uniform distribution (2) on  [0.5,1.0]×[0.5,1.0] from
iterations  5000 to 10000,  a uniform  distribution (3)  on [0.0,0.5]×[0.5,1.0]
from  iterations  10000  to 15000  and  a  final  uniform distribution  (4)  on
[0.5,1.0]×[0.0,0.5] from iterations 15000  to 20000. NG shows some difficulties
in tracking  various changes and  the final state  reflects the history  of the
distribution: there are many code  words within the first distribution and very
few in the  final one. In the case  of SOM, the algorithm can  almost cope with
the  dynamic nature  of the  distributions  as long  as its  learning rate  and
neighbourhood function are large enough to  move the codebook into the new data
region. This  is the  case for distributions  (1) to  (3) but the  final change
makes the SOM network unable to  map the final distribution as expected because
of the time  dependency of the algorithm.  In the case of DSOM,  the network is
able to  accurately track each  successive distribution with a  short transient
error correlated to  the distribution change. We think  this behaviour reflects
cortical  plasticity  seen  as a  tight  coupling  between  the model  and  the
environment.

.. figure:: images/dynamic.png
   :target: images/dynamic.png
   :label:  dynamic

   Three networks (NG, SOM, DSOM) have  been trained for 20 000 iterations on a
   dynamic distribution  that vary  along time: a  uniform distribution  (1) on
   [0.0,0.5]×[0.0,0.5] from iterations 0 to 5000, a uniform distribution (2) on
   [0.5,1.0]×[0.5,1.0] from  iterations 5000  to 10000, a  uniform distribution
   (3)  on [0.0,0.5]×[0.5,1.0]  from  iterations  10000 to  15000  and a  final
   uniform  distribution (4)  on [0.5,1.0]×[0.0,0.5]  from iterations  15000 to
   20000.


High-dimensional distributions                                                 
-------------------------------------------------------------------------------
Until now, we have  considered only trivial two-dimensional distributions whose
intrinsic  dimension matched  the topography  of the  network. We  now consider
higher dimensional  distribution with  unknown intrinsic dimension.   Using the
standard Lena  grey-level image as a  source input, samples of  8×8 pixels have
been  draw   uniformly  from   the  image  and   presented  to   the  different
networks. 1000 such samples have been  drawn and all three networks have learnt
during  10 000  iterations. As  illustrated on  figure :fig:`lena`,  the strong
influence of neighbourhood  in the case of SOM leads to  a final codebook where
vectors tend  to be very homogeneous and  composed of a mean  value with little
variations around  this mean  value. In  the case of  NG, things  are different
because of the absence of  topographic constraints: NG converges rapidly toward
a stable  solution made  of qualitatively different  filters, part of  them are
quite  homogeneous  like in  SOM  but some  others  clearly  possess a  greater
internal  variety. In  the case  of DSOM,  we can  also check  on the  figure a
greater variety of filters that are self-organised.

.. figure:: images/lena.png
   :target: images/lena.png
   :label:  lena

   Three networks  (NG, SOM, DSOM) have  been trained for 20  000 iterations on
   1000 samples  of size  8×8 pixels  that have been  drawn uniformly  from the
   standard lena grey image.

The  meaning of  such a  greater variety  of  filters in  the case  of DSOM  is
difficult  to appreciate.  In  the one  hand,  if we  were  to reconstruct  the
original  image  using  those  filters,  we would  certainly  obtain  a  larger
distortion error. In the other hand,  if those filters were supposed to extract
useful information from  the image, they would certainly  give a better account
of the structure of the image.


Conclusion                                                                     
===============================================================================
One of the major problem of most neural map algorithms is the necessity to have
a finite set  of observations to perform adaptive learning  starting from a set
of  initial parameters (learning  rate, neighbourhood  or temperature)  at time
`t_i` down  to a set  of final  parameters at time  `t_f`. In the  framework of
signal processing  or data analysis, this may  be acceptable as long  as we can
generate a finite set of samples in order to learn it off-line. However, from a
more behavioural point of view, this is not always possible to have access to a
finite set and we must face on-line learning. As explained in the introduction,
if  we consider  the  existence of  a critical  period  in the  early years  of
development,  the problem  may be  solved  using decreasing  learning rate  and
neighbourhood over an extended period of  time. But if this may explain to some
extents  the development  of early  sensory filters,  this fails  at explaining
cortical   plasticity    at   a   more   broad   level.     As   explained   in
[Buonomano+Al:1998]_,  we know  today that  *"cortical representations  are not
fixed  entities, but  rather,  are  dynamic and  are  continuously modified  by
experience"*. How can we achieve both stability and reactivity ?

We proposed  to answer this question  by introducing a variant  of the original
SOM learning algorithm  where time depency has been  removed. With no available
formal  proof  of  convergence  and   based  on  several  experiments  in  both
two-dimensional, high-dimensional  cases and dynamic  cases, we think  this new
algorithm allows for on-line and  continuous learning ensuring a tight coupling
to the environment.  However, the resulting codebook does  not fit data density
as expected  in most  VQ algorithms. This  could be  a serious drawback  in the
framework  of signal  processing or  data compression  but may  be  a desirable
property  from a  behavioural point  fo  view. For  example let  us consider  a
picture of a (very) snowy landscape with a small tree in the middle. If we want
to mimic  visual exploration of the  scene using eye saccades,  we can randomly
pick small  patches within the  image and present  them to the model.  Not very
surprisingly, the  vast majority  of these patches  would be  essentially white
(possibly with some variations) because the whole image is mainly white. From a
pure VQ point of view, the codebook would reflect this density by having a vast
majority of its representations into the  white domain and if the tree is small
enough, we could even have only white representation within the codebook. While
this would serve data  compression, how much is it relevant in  general ? We do
not have  the answer  in the  general case but  we think  this must  be decided
explicitely depending on task. DSOM allows such explicit decision since it maps
the structure of the data rather than  their density. This means that in a more
general framework, we could expect an external structure to attach some kind of
motivation for  each data that would  modulate its learning. If  some region of
the  perceptive space  is judged  behaviourally relevant,  model  could develop
precise representations in this region but if learning is driven solely by data
density  (like  in  most  VQ),  such modulation  would  certainly  be  strongly
attenuated or not possible at all.


Appendix A                                                                     
===============================================================================
.. nosectnum::

Here  are  some  results  linked  to various  distributions  illustrating  both
differences between NG, SOM and DSOM as well as DSOM specific properties.

.. figure:: images/uniform.png
   :target: images/uniform.png
 
   Three 8×8 networks  (NG, SOM, DSOM) have been trained  for 20 000 iterations
   on a uniform  square distribution using 10 000  samples.  Initialisation has
   been done by placing initial code vectors randomly over the [0,1]² area.


.. figure:: images/ring.png
   :target: images/ring.png

   Three 8×8 networks  (NG, SOM, DSOM) have been trained  for 20 000 iterations
   on a ring distribution using 10 000 samples. Initialisation has been done by
   placing initial code vectors randomly over the [0,1]² area.


.. figure:: images/double-ring.png
   :target: images/double-ring.png

   Three 8×8 networks  (NG, SOM, DSOM) have been trained  for 20 000 iterations
   on a uniform double  ring-distribution using 10 000 samples.  Initialisation
   has been done by placing initial code vectors randomly over the [0,1]² area.


.. figure:: images/gaussian-filters.png
   :target: images/gaussian-filters.png


   Three 8×8 networks  (NG, SOM, DSOM) have been trained  for 20 000 iterations
   on a set  of noisy rotated elongated Gaussians whose  angles have been drawn
   from a uniform distribution in  [-π/2,+π/2] .  An input is represented
   as a two-dimensional 16×16 vector  of real values (∈ [0,1]) and additive
   noise has been added using uniform random variables in [-0.1,0.1].


Appendix B                                                                     
===============================================================================
.. nosectnum::

.. figure:: movies/sphere.avi, movies/sphere.ogg
   :controls:
   :figwidth: 45%
   :figclass: right

   A 32×32 DSOM has been trained for 10000 iterations on a set of 10 000 points
   uniformly distributed over the surface of a sphere of radius 0.5 centered at
   (0.5,0.5,0.5).  Initialisation has been done by placing initial code vectors
   at the center of the sphere and elasticity has been set to 1.0.

.. figure:: movies/cube.avi, movies/cube.ogg
   :controls:
   :figwidth: 45%
   :figclass: clear-left

   A 32×32 DSOM has been trained for 10000 iterations on a set of 10 000 points
   uniformly distributed over  the surface of a cube of  radius 0.5 centered at
   (0.5,0.5,0.5).  Initialisation has been done by placing initial code vectors
   at the center of the sphere and elasticity has been set to 1.0.


.. figure:: movies/sphere-spheres.avi, movies/sphere-spheres.ogg
   :controls:
   :figwidth: 45%
   :figclass: right

   Self-reorganization from sphere to spheres surface

.. figure:: movies/sphere-cube.avi, movies/sphere-cube.ogg
   :controls:
   :figwidth: 45%
   :figclass: clear-left

   Self-reorganization from sphere to cubic surface



References                                                                     
===============================================================================
.. nosectnum::

.. [BachyRita+Al:1969] P. B. y Rita, C. Collins, F. Saunders, B. White, and
   L. Scadden. Vision substitution by tactile image projection. In *Nature*,
   221:963-964, 1969.

.. [BachyRita:1972] P. BachyRita. *Brain Mechanisms in Sensory Substitution*.
   Academic Press New York, 1972.

.. [Buonomano+Al:1998] D. Buonomano, M. Merzenich, Cortical plasticity: From
   synapses to maps, *Annual Review of Neuroscience* 21 (1998) 149--186.

.. [Cottrel+Al:1998] M. Cottrell, J. Fort, G. Pagès, Theoretical aspects of the
   som algorithm, *Neurocomputing* 21 (1998) 119--138.

.. [Cottrell+Al:1987] M. Cottrell, J. Fort, Etude d'un algorithme
   d'auto-organisation, *Annales Institut Henri Poincaré* 23~(1) (1987) 1--20.

.. [Daw:1994] N. Daw. Mechanisms of plasticity in the visual  cortex. In
   *Investigative Ophthalmology*, 35:4168-4179, 1994.

.. [Deng+Al:2000] D. Deng, N. Kasabov, Esom: An algorithm to evolve
   self-organizing maps from on-line data streams, in: *Proc. of IJCNN'2000*,
   Vol. VI, Como, Italy, 2000, pp. 3--8.

.. [Deng+Al:2003] D. Deng, N. Kasabov, On-line pattern analysis by evolving
   self-organizing maps, *Neurocomputing* 51 (2003) 87--103.

.. [Durbin+Willshaw:1987] R. Durbin, D. Willshaw, An analogue approach to the
   travelling salesman problem. In *Nature* 326 (1987) 689-691.

.. [Erwin+Al:1992] E. Erwin, K. Obermayer, K. Schulten, Self-organizing maps:
   Ordering, convergence properties and energy functions, *Biological
   Cybernetics* 67 (1992) 47--55.

.. [Fritzke:1995] B. Fritzke. A growing neural gas network learns topologies.
   In G. Tesauro, D. Touretzky, and T. Leen, editors, *Advances in Neural
   Information Processing Systems 7*, pages 625-632. MIT Press, Cambridge MA,
   1995.

.. [Fritzke:1997] B. Fritzke, A self-organizing network that can follow
   non-stationary distributions, in: *ICANN*, 1997, pp. 613--618.

.. [Furao+Al:2006] S. Furao, O. Hasegawa, An incremental network for on-line
   unsupervised classification and topology learning, *Neural Networks* 19 (1)
   (2006) 90--106.

.. [Furao+Al:2007] S. Furao, T. Ogura, O. Hasegawa, An enhanced self-organizing
   incremental neural network for online unsupervised learning, *Neural
   Networks* 20 (8) (2007) 893--903.

.. [Grossberg:1987] S. Grossberg, Competitive learning: From interactive
   activation to adaptive resonance. In *Cognitive Science* 11(1) (1987)
   23-63.

.. [Heskes:1999] T. Heskes, Energy functions for self-organizing maps, in:
   E. Oja, S. Kaski(Eds.), *Kohonen Maps*, Elsevier, Amsterdam, 1999,
   pp. 303--315.

.. [Hubel+Wiesel:1965] D. Hubel and T. Wiesel. Receptive fields and functional
   architecture in two non-striate visual areas (18 and 19) of the
   cat. In *Journal of Neurophysiology*, 28:229-289, 1965.

.. [Hubel+Wiesel:1970] D. Hubel and T. Wiesel. The period of susceptibility to
   the physiological effects of unilateral eye closure in kittens. In *Journal
   of Physiology*, 206:419-436, 1970.

.. [Kaski+Al:1998] S. Kaski, J. Kangas, T. Kohonen, Bibliography of
   self-organizing map (som) papers: 1981-1997, *Neural Computing Surveys* 1
   (1998) 102--320.

.. [Keith-Magee:2001] R. Keith-Magee, Learning and development in kohonen-style
   self-organising maps, Ph.D. thesis, Curtin University of Technology (2001).

.. [Kohonen:1982] T. Kohonen. Self-organized formation of topologically correct
   feature maps. In *Biological Cybernetics*, 43:59-69, 1982.

.. [Linde+Al:1980] A. B. Linde, A. Buzo and R. Gray. An algorithm for vector
   quantization design. In *IEEE Trans. on Communications*, COM-28:84-95, 1980.

.. [MacQueen:1967] J. B. Macqueen. Some methods of classification and analysis
   of multivariate observations. In *Proceedings of the Fifth Berkeley
   Symposium on Mathematical Statistics and Probability*, pages 281-297, 1967.

.. [Martinetz+Al:1993] T. M. Martinetz, S. G. Berkovich, and  K. J. Schulten.
   Neural-gas network for vector quantization and its application to
   time-series prediction. In *IEEE Trans. on Neural Networks*, 4(4):558-569,
   1993.

.. [Oja+Al:2003] M. Oja, S. Kaski, T. Kohonen, Bibliography of self-organizing
   map (som) papers: 1998-2001 addendum, *Neural Computing Surveys* 3 (2003)
   1--156.

.. [Pöllä+Al:2009] M. Pöllä, T. Honkela, T. Kohonen, Bibliography of
   self-organizing map (som) papers: 2002-2005 addendum, Tech. rep.,
   Information and Computer Science, Helsinki University of Technology (2009).

.. [Ramachadran+Al:1992] V. Ramachandran, D. Rogers-Ramachandran, and
   M. Stewart. Perceptual correlates of massive cortical reorganization. In
   *Science*, 258:1159-1160, 1992.

.. [Villman+Clausen:2006] T. Villman, J. Claussen, Magnification control in
   self-organizing maps and neural gas. In *Neural Computation* 18 (2006)
   446-449.



About this document                                                            
===============================================================================
.. nosectnum::

This document has  been generated using a modified  version of the `rst2html.py
<rst2html.py>`_ python script for  converting a restructured text document into
an  html   one.   The   rst  source  of   this  document  is   avalaible  `here
<article.rst.html>`_.
