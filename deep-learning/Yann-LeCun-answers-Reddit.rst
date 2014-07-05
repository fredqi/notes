
========================================
Yann LeCun's answers from the Reddit AMA
========================================

:URL: http://fastml.com/yann-lecuns-answers-from-the-reddit-ama/

On May 15th Yann LeCun answered "ask me anything" questions on
`Reddit <http://www.reddit.com/r/MachineLearning/comments/25lnbt/ama_yann_lecun/?limit=500>`__.
We hand-picked some of his thoughts and grouped them by topic for your
enjoyment.


Toronto, Montreal and New York
------------------------------

All three groups are strong and complementary.

Geoff (who spends more time at Google than in Toronto now) and Russ
Salakhutdinov like RBMs and deep Boltzmann machines. I like the idea of
Boltzmann machines (it's a beautifully simple concept) but it doesn't
scale well. Also, I totally hate sampling.

Yoshua and his colleagues have focused a lot on various unsupervised
learning, including denoising auto-encoders, contracting auto-encoders.
They are not allergic to sampling like I am. On the application side,
they have worked on text, not so much on images.

In our lab at NYU (Rob Fergus, David Sontag, me and our students and
postdocs), we have been focusing on sparse auto-encoders for
unsupervised learning. They have the advantage of scaling well. We have
also worked on applications, mostly to visual perception.

Numenta, Vicarious, NuPic, HTM, CLA, etc.
-----------------------------------------

Jeff Hawkins has the right intuition and the right philosophy. Some of
us have had similar ideas for several decades. Certainly, we all agree
that AI systems of the future will be hierarchical (it's the very idea
of deep learning) and will use temporal prediction.

But the difficulty is to instantiate these concepts and reduce them to
practice. Another difficulty is grounding them on sound mathematical
principles (is this algorithm minimizing an objective function?).

I think Jeff Hawkins, Dileep George and others greatly underestimated
the difficulty of reducing these conceptual ideas to practice.

As far as I can tell, HTM has not been demonstrated to get anywhere
close to state of the art on any serious task.

--------------

I still think [Vicarious] is mostly hype. There is no public information
about the underlying technology. The principals don't have a
particularly good track record of success. And the only demo is way
behind what you can do with "plain vanilla" convolutional nets (see this
Google blog post and this ICLR 2014 paper and this video of the ICLR
talk).

--------------

HTM, NuPIC, and Numenta received a lot more publicity than they deserved
because of the Internet millionaire / Silocon Valley celebrity status of
Jeff Hawkins.

But I haven't seen any result that would give substance to the hype.

--------------

Don't get fooled by people who claim to have a solution to Artificial
General Intelligence, who claim to have AI systems that work "just like
the human brain", or who claim to have figured out how the brain works
(well, except if it's Geoff Hinton making the claim). Ask them what
error rate they get on MNIST or ImageNet.


Some advice
-----------

Seriously, I don't like the phrase "Big Data". I prefer "Data Science",
which is the automatic (or semi-automatic) extraction of knowledge from
data. That is here to stay, it's not a fad. The amount of data generated
by our digital world is growing exponentially with high rate (at the
same rate our hard-drives and communication networks are increasing
their capacity). But the amount of human brain power in the world is not
increasing nearly as fast. This means that now or in the near future
most of the knowledge in the world will be extracted by machine and
reside in machines. It's inevitable. En entire industry is building
itself around this, and a new academic discipline is emerging.

--------------

**What areas do you think are most promising right now for people who
are just starting out?**

-  representation learning (the current crop of deep learning methods is
   just one way of doing it)
-  learning long-term dependencies
-  marrying representation learning with structured prediction and/or
   reasoning
-  unsupervised representation learning, particularly prediction-based
   methods for temporal/sequential signals
-  marrying representation learning and reinforcement learning
-  using learning to speed up the solution of complex inference problems
-  theory: do theory (any theory) on deep learning/representation
   learning
-  understanding the landscape of objective functions in deep learning
-  in terms of applications: natural language understanding (e.g. for
   machine translation), video understanding
-  learning complex control.

--------------

**Do you think that deep learning would be a good tool for finding
similarities in the medical domain (e.g. between different cases)?**

Yes, look up papers on metric learning, searching for "siamese
networks", DrLIM (Dimensionality Reduction by Learning and Invariant
Mapping), NCA (Neigborhood Component Analysis), WSABIE….

--------------

Larger networks tend to work better. Make your network bigger and bigger
until the accuracy stops increasing. Then regularize the hell out of it.
Then make it bigger still and pre-train it with unsupervised learning.

--------------

Speech is one of those domains where we have access to ridiculously
large amounts of data and a very large number of categories. So, it's
very favorable for supervised learning.

--------------

**There are theoretical results that suggest that learning good
parameter settings for a (smallish) neural network can be as hard
computationally as breaking the RSA crypto system.**

The limitations you point out do not concern just backprop, but all
learning algorithms that use gradient-based optimization.

These methods only work to the extent that the landscape of the
objective function is well behaved. You can construct pathological cases
where the objective function is like a golf course: flat with a tiny
hole somewhere. Gradient-based methods won't work with that.

The trick is to stay away from those pathological cases. One trick is to
make the network considerably larger than the minimum size required to
solve the task. This creates lots and lots of equivalent local minima
and makes them easy to find. The problem is that large networks may
overfit, and we may have to regularize the hell out of them (e.g. using
drop out).

The "learning boolean formula = code cracking" results pertain to
pathological cases and to exact solutions. In most applications, we only
care about approximate solutions.


Physics
-------

I learned a lot by reading things that are not apparently connected with
AI or computer science (my undergraduate degree is in electrical
engineering, and my formal CS training is pretty small).

For example, I have always been interested in physics, and I have read
tons of physics textbooks and papers. I learned a lot about path
integrals (which is formally equivalent to the "forward algorithm" in
hidden Markov models). I have also learned a ton from statistical
physics books. The notions of partition functions, entropy, free energy,
variational methods etc, that are so prevalent in the graphical models
literature all come from statistical physics.

--------------

In the early 90's my friend and Bell Labs colleague John Denker and I
worked quite a bit on the physics of computation.

In 1991, we attended a workshop at the Santa Fe Institute in which we
heard a fascinating talk by John Archibald Wheeler entitled "It from
Bits". John Wheeler was the theoretical physicist who coined the phrase
"black hole". Many physicists like Wojciech Zurek (the organizer of the
workshop, Gerard T'Hooft, and many others have the intuition that
physics can be reduced to information transformation.

Like Kolmogorov, I am fascinated by the concept of complexity, which is
at the root of learning theory, compression, and thermodynamics. Zurek
has an interesting series of work on a definition of physical entropy
that uses Kolmogorov/Chaitin/Solomonoff algorithmic complexity. But
progress has been slow.

Fascinating topics.

Most of my Bell Labs colleagues were physicists, and I loved interacting
with them.

--------------

Physics is about modeling actual systems and processes. It's grounded in
the real world. You have to figure out what's important, know what to
ignore, and know how to approximate. These are skills you need to
conceptualize, model, and analyze ML models.


Math
----

I use a lot of math, sometimes at the conceptual level more than at the
"detailed proof" level. A lot of ideas come from mathematical intuition.
Proofs always come later. I don't do a lot of proofs. Others are better
than me at proving theorems.

--------------

There is a huge amount of interest for representation learning from the
applied mathematics community. Being a faculty member at the Courant
Institute of Mathematical Science at NYU, which is ranked #1 in applied
math in the US, I am quite familiar with the world of applied math (even
though I am definitely not a mathematician).

Theses are folks who have long been interested in representing data
(mostly natural signals like audio and images). These are people who
have worked on wavelet transforms, sparse coding and sparse modeling,
compressive sensing, manifold learning, numerical optimization,
scientific computing, large-scale linear algebra, fast transform (FFT,
Fast Multipole methods). This community has a lot to say about how to
represent data in high-dimensional spaces.

In fact, several of my postdocs (e.g. Joan Bruna, Arthur Szlam) have
come from that community because I think they can help with cracking the
unsupervised learning problem.

I do not believe that classical learning theory with "IID samples,
convex optimization, and supervised classification and regression" is
sufficient for representation learning. SVM do not naturally emerge from
VC theory. SVM happen to simple enough for VC theory to have specific
results about them. Those results are cool and beautiful, but they have
no practical consequence. No one uses generalization bounds to do model
selection. Everyone in their right mind use (cross)validation.

The theory of deep learning is a wide open field. Everything is up for
the taking. Go for it.

--------------

**How do you approach utilizing and researching machine learning
techniques that are supported almost entirely empirically, as opposed to
mathematically? Also in what situations have you noticed some of these
techniques fail?**

You have to realize that our theoretical tools are very weak. Sometimes,
we have good mathematical intuitions for why a particular technique
should work. Sometimes our intuition ends up being wrong.

Every reasonable ML technique has some sort of mathematical guarantee.
For example, neural nets have a finite VC dimension, hence they are
consistent and have generalization bounds. Now, these bounds are
terrible, and cannot be used for any practical purpose. But every single
bound is terrible and useless in practice (including SVM bounds).

As long as your method minimizes some sort of objective function and has
a finite capacity (or is properly regularized), you are on solid
theoretical grounds.

The questions become: how well does my method work on this particular
problem, and how large is the set of problems on which it works well.


Kernel methods
--------------

Kernel methods are great for many purposes, but they are merely
glorified template matching. Despite the beautiful math, a kernel
machine is nothing more than one layer of template matchers (one per
training sample) where the templates are the training samples, and one
layer of linear combinations on top.

There is nothing magical about margin maximization. It's just another
way of saying "L2 regularization" (despite the cute math).

--------------

Let me be totally clear about my opinion of kernel methods. I like
kernel methods (as Woody Allen would say "some of my best friends are
kernel methods"). Kernel methods are a great generic tool for
classification. But they have limits, and the cute mathematics that
accompany them does not give them magical properties. SVMs were invented
by my friends and colleagues at Bell Labs, Isabelle Guyon, Vladimir
Vapnik, and Bernhardt Boser, and later refined by Corinna Cortes and
Chris Burges. All these people and I were members of the Adaptive
Systems Research Department lead by Larry Jackel. We were all sitting in
the same corridor in AT&T Bell Labs' Holmdel building in New Jersey. At
some point I became the head of that group and was Vladimir's boss.
Other people from that group included Leon Bottou and Patrice Simard
(now both at Microsoft Research). My job as the department head was to
make sure people like Vladimir could work on their research with minimal
friction and distraction. My opinion of kernel method has not changed
with the emergence of MKL and metric learning. I proposed/used metric
learning to learn embeddings with neural nets before it was cool to do
this with kernel machines. Learning complex/hierarchical/non-linear
features/representations/metrics cannot be done with kernel methods as
it can be done with deep architectures. If you are interested in metric
learning, look up
`this <http://yann.lecun.com/exdb/publis/index.html#bromley-94>`__,
`this <http://yann.lecun.com/exdb/publis/index.html#chopra-05>`__, or
`that <http://yann.lecun.com/exdb/publis/index.html#hadsell-chopra-lecun-06>`__.


ConvNets
--------

It's important to remind people that convolutional nets were
***always*** the record holder on MNIST. SVMs never really managed to
beat ConvNets on MNIST. And SVMs (without hand-crafted features and with
a generic kernel) were always left in the dust on more complex image
recognition problems (e.g. NORB, face detection….).

The first commercially-viable check reading system (deployed by AT&T/NCR
in 1996) used a ConvNet, not an SVM.

Getting the attention of the computer vision community was a struggle
because, except for face detection and handwriting recognition, the
results of supervised ConvNets on the standard CV benchmarks were OK but
not great. This was largely due to the fact that the training sets were
very small. I'm talking about the Caltech-101, Caltech-256 and PASCAL
datasets.

We had excellent, record-breaking results on a number of tasks like
semantic segmentation, pedestrian detection, face detection, road sign
recognition and a few other problems. But the CV community played little
attention to it.

As soon as ImageNet came out and as soon as we figured out how to train
gigantic ConvNets on GPUs, ConvNets took over. That struggle took time,
but in the end people are swayed by results.

I must say that many senior members of the CV community were very
welcoming of new ideas. I really feel part of the CV community, and I
hold no grudge against anyone. Still, for the longest time, it was very
difficult to get ConvNet papers accepted in conferences like CVPR and
ICCV until last year (even at NIPS until about 2007).


Deconvolutional networks
~~~~~~~~~~~~~~~~~~~~~~~~

DeconvNets are the generative counterpart of feed-forward ConvNets.

Eventually, we will figure out how to merge ConvNet and DeconvNet so
that we have a feed-forward+feed-back system that can be trained
supervised or unsupervised.

The plan Rob Fergus and I devised was always that we would eventually
marry the two approaches.


Unsupervised learning
---------------------

The interest of the ML community in representation learning was
rekindled by early results with unsupervised learning: stacked sparse
auto-encoders, RBMs, etc. It is true that the recent practical success
of deep learning in image and speech all use purely supervised backprop
(mostly applied to convolutional nets). This success is largely due to
dramatic increases in the size of datasets and the power of computers
(brought about by GPU), which allowed us to train gigantic networks
(often regularized with drop-out). Still, there are a few applications
where unsupervised pre-training does bring an improvement over purely
supervised learning. This tends to be for applications in which the
amount of labeled data is small and/or the label set is weak. A good
example from my lab is pedestrian detection. Our CVPR 2013 paper shows a
big improvement in performance with ConvNets that unsupervised
pre-training (convolutional sparse auto-encoders). The training set is
relatively small (INRIA pedestrian dataset) and the label set is weak
(pedestrian / non pedestrian). But everyone agrees that the future is in
unsupervised learning. Unsupervised learning is believed to be essential
for video and language. Few of us believe that we have found a good
solution to unsupervised learning.

--------------

I don't believe that there is a single criterion to measure the
effectiveness of unsupervised learning.

Unsupervised learning is about discovering the internal structure of the
data, discovering mutual dependencies between input variables, and
disentangling the independent explanatory factors of variations.
Generally, unsupervised learning is a means to an end.

There are four main uses for unsupervised learning: 1. learning features (or
representations) 2. visualization/exploration 3. compression 4. synthesis

Only the first is interesting to me (the other uses are interesting too,
just not on my own radar screen).

If the features are to be used in some sort of predictive model
(classification, regression, etc), then that's what we should use to
measure the performance of our algorithm.

Torch
-----

(At Facebook) We are using `Torch7 <http://torch.ch/>`__ for many
projects (as does Deep Mind and several groups at Google) and will be
contributing to the public version.

--------------

Torch is a numerical/scientific computing extension of LuaJIT with an
ML/neural net library on top.

The huge advantage of LuaJIT over Python is that it way, way faster,
leaner, simpler, and that interfacing C/C++/CUDA code to it is
incredibly easy and fast.

We are using Torch for most of our research projects (and some of our
development projects) at Facebook. Deep Mind is also using Torch in a
big way (largely because my former student and Torch-co-maintainer Koray
Kavukcuoglu sold them on it). Since the Deep Mind acquisition, folks in
the Google Brain group in Mountain View have also started to use it.

Facebook, NYU, and Google/Deep Mind all have custom CUDA back-ends for
fast/parallel convolutional network training. Some of this code is not
(yet) part of the public distribution.

--------------

You could say that Torch is the direct heir of Lush, though the
maintainers are different.

Lush was mostly maintained by Leon Bottou and me. Ralf Juengling took
over the development of Lush2 a few years ago.

Torch is maintained by Ronan Collobert (IDIAP), Koray Kavukcuoglu (Deep
Mind. former s=PhD student of mine) and Clément Farabet (running his own
startup. Also a former PhD student of mine). We have used Torch as the
main research platform in my NYU lab for quite a while.

--------------

Here is a `tutorial <http://code.madbits.com/wiki/doku.php>`__, with
code.scripts for ConvNets.

Also, the wonderful `Torch7
Cheatsheet <https://github.com/torch/torch7/wiki/Cheatsheet>`__.

Torch7 is what is being used for deep learning R&D at NYU, at Facebook
AI Research, at Deep Mind, and at Google Brain.


The future
----------

Deep learning has become the dominant method for acoustic modeling in
speech recognition, and is quickly becoming the dominant method for
several vision tasks such as object recognition, object detection, and
semantic segmentation.

The next frontier for deep learning are language understanding, video,
and control/planning (e.g. for robotics or dialog systems).

Integrating deep learning (or representation learning) with reasoning
and making unsupervised learning actually work are two big challenges
for the next several years.

--------------

The direction of history is that the more data we get, the more our
methods rely on learning. Ultimately, the task use learning end to end.
That's what happened for speech, handwriting, and object recognition.
It's bound to happen for NLP.

--------------

Natural language processing is the next frontier for deep learning.
There is a lot of research activity in that space right now.

--------------

There is a lot of interesting work on neural language models and
recurrent nets from Yoshua Bengio, Toma Mikolov, Antoine Bordes and
others.

--------------

Integrating deep learning (or representation learning) with reasoning
and making unsupervised learning actually work are two big challenges
for the next several years.

--------------

**What are some of the important problems in the field of AI/ML that
need to be solved within the next 5-10 years?**

Learning with temporal/sequential signals: language, video, speech.

Marrying deep/representation learning with reasoning or structured
prediction.

--------------

**What do you think are the biggest applications machine learning will
see in the coming decade?**

Natural language understanding and natural dialog systems. Self-driving
cars. Robots (maintenance robots and such).


Epilogue
--------

That's all, folks. If you want more, there's the `NYU Course on Big
Data, Large Scale Machine
Learning <http://techtalks.tv/nyu/nyu-course-on-large-scale-machine-learning/>`__
with Yann and John Langford as instructors and `materials for the 2014
Deep Learning
Course <http://cilvr.nyu.edu/doku.php?id=deeplearning:slides:start>`__,
including some videos.

