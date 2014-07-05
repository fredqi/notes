
=================================
Python Tools for Machine Learning
=================================

:URL: http://www.cbinsights.com/blog/python-tools-machine-learning

Python is one of the best programming languages out there, with an
extensive coverage in scientific computing: computer vision, artificial
intelligence, mathematics, astronomy to name a few. Unsurprisingly, this
holds true for machine learning as well.

Of course, it has some disadvantages too; one of which is that the tools
and libraries for Python are scattered. If you are a unix-minded person,
this works quite conveniently as every tool does one thing and does it
well. However, this also requires you to know different libraries and
tools, including their advantages and disadvantages, to be able to make
a sound decision for the systems that you are building. Tools by
themselves do not make a system or product better, but with the right
tools we can work much more efficiently and be more productive.
Therefore, knowing the right tools for your work domain is crucially
important.

This post aims to list and describe the most useful machine learning
tools and libraries that are available for Python. To make this list, we
did not require the library to be written in Python; it was sufficient
for it to have a Python interface. We also have a small section on Deep
Learning at the end as it has received a fair amount of attention
recently.

We do not aim to list **all** the machine learning libraries available
in Python (the Python package index returns 139 results for “machine
learning”) but rather the ones that we found useful and well-maintained
to the best of our knowledge. Moreover, although some of modules could
be used for various machine learning tasks, we included libraries whose
main focus is machine learning. For example,
although `Scipy <http://docs.scipy.org/doc/scipy/reference/index.html>`__ has
some `clustering
algorithms <http://docs.scipy.org/doc/scipy/reference/cluster.vq.html#module-scipy.cluster.vq>`__,
the main focus of this module is not machine learning but rather in
being a comprehensive set of tools for scientific computing. Therefore,
we excluded libraries like Scipy from our list (though we use it too!).

Another thing worth mentioning is that we also evaluated the library
based on how it integrates with other scientific computing libraries
because machine learning (either supervised or unsupervised) is part of
a data processing system. If the library that you are using does not fit
with your rest of data processing system, then you may find yourself
spending a tremendous amount of time to creating intermediate layers
between different libraries. It is important to have a great library in
your toolset but it is also important for that library to integrate well
with other libraries.

If you are great in another language but want to use Python packages, we
also briefly go into how you could integrate with Python to use the
libraries listed in the post.

Scikit-Learn
============

`Scikit Learn <http://scikit-learn.org/stable/>`__ is our machine
learning tool of choice at CB Insights. We use it for classification,
feature selection, feature extraction and clustering. What we like most
about it is that it has a consistent API which is easy to use while also
providing **a lot of** evaluation, diagnostic and cross-validation
methods out of the box (sound familiar? Python has batteries-included
approach as well). The icing on the cake is that it uses Scipy data
structures under the hood and fits quite well with the rest of
scientific computing in Python with Scipy, Numpy, Pandas and Matplotlib
packages. Therefore, if you want to visualize the performance of your
classifiers (say, using a precision-recall graph or Receiver Operating
Characteristics (ROC) curve) those could be quickly visualized with help
of Matplotlib. Considering how much time is spent on cleaning and
structuring the data, this makes it very convenient to use the library
as it tightly integrates to other scientific computing packages.

Moreover, it has also limited Natural Language Processing feature
extraction capabilities as well such as bag of words, tfidf,
preprocessing (stop-words, custom preprocessing, analyzer). Moreover, if
you want to quickly perform different benchmarks on toy datasets, it has
a datasets module which provides common and useful datasets. You could
also build toy datasets from these datasets for your own purposes to see
if your model performs well before applying the model to the real-world
dataset. For parameter optimization and tuning, it also provides grid
search and random search. These features could not be accomplished if it
did not have great community support or if it was not well-maintained.
We look forward to its first stable release.

Statsmodels
===========

`Statsmodels <http://statsmodels.sourceforge.net/>`__ is another great
library which focuses on statistical models and is used mainly for
predictive and exploratory analysis. If you want to fit linear models,
do statistical analysis, maybe a bit of predictive modeling, then
Statsmodels is a great fit. The statistical tests it provides are quite
comprehensive and cover validation tasks for most of the cases. If you
are R or S user, it also accepts R syntax for some of its statistical
models. It also accepts Numpy arrays as well as Pandas data-frames for
its models making creating intermediate data structures a thing of the
past!

PyMC
====

`PyMC <http://pymc-devs.github.io/pymc/>`__ is the tool of choice
for **Bayesians**. It includes Bayesian models, statistical
distributions and diagnostic tools for the convergence of models. It
includes some hierarchical models as well. If you want to do Bayesian
Analysis, you should check it out.

Shogun
======

`Shogun <http://www.shogun-toolbox.org/page/home/>`__ is a machine
learning toolbox with a focus on Support Vector Machines (SVM) that is
written in C++. It is actively developed and maintained, provides a
Python interface and the Python interface is mostly documented well.
However, we’ve found its API hard to use compared to Scikit-learn. Also,
it does not provide many diagnostics or evaluation algorithms out of the
box. However, its speed is a great advantage.

Gensim
======

`Gensim <http://radimrehurek.com/gensim/>`__ is defined as “topic
modeling for humans”. As its homepage describes, its main focus is
Latent Dirichlet Allocation (LDA) and its variants. It also has some
classification capabilities but it is not what it is most commonly used
for. Different from other packages, it has support for Natural Language
Processing which makes it easier to combine NLP pipeline with other
machine learning algorithms. If your domain is in NLP and you want to do
clustering and basic classification, you may want to check it out.
Recently, they introduced Recurrent Neural Network based text
representation called word2vec from Google to their API as well. This
library is written purely in Python.

Orange
======

`Orange <http://orange.biolab.si/>`__ is the only library that has a
Graphical User Interface (GUI) among the libraries listed in this post.
It is also quite comprehensive in terms of classification, clustering
and feature selection methods and has some cross-validation methods. It
is better than Scikit-learn in some aspects (classification methods,
some preprocessing capabilities) as well, but it does not fit well with
the rest of the scientific computing ecosystem (Numpy, Scipy,
Matplotlib, Pandas) as nicely as Scikit-learn.

Having a GUI is an important advantage over other libraries however. You
could visualize cross-validation results, models and feature selection
methods (you need to install Graphviz for some of the capabilities
separately). Orange has its own data structures for most of the
algorithms so you need to wrap the data into Orange-compatible data
structures which makes the learning curve steeper.

PyMVPA
======

`PyMVPA <http://www.pymvpa.org/index.html>`__ is another statistical
learning library which is similar to Scikit-learn in terms of its API.
It has cross-validation and diagnostic tools as well, but it is not as
comprehensive as Scikit-learn.

Deep Learning
=============

Even though deep learning is a subsection Machine Learning, we created a
separate section for this field as it has received tremendous attention
recently with various acqui-hires by Google and Facebook.

Theano
------

`Theano <http://deeplearning.net/software/theano/>`__ is the most mature
of deep learning library. It provides nice data structures (tensors) to
represent layers of neural networks and they are efficient in terms of
linear algebra similar to Numpy arrays. One caution is that, its API may
not be very intuitive, which increases learning curve for users. There
are a lot of
`libraries <https://github.com/Theano/Theano/wiki/Related-projects>`__
which build on top of Theano exploiting its data structures. It has
support for GPU programming out of the box as well.

PyLearn2
--------

There is another library built on top of Theano,
called \ `PyLearn2 <http://deeplearning.net/software/pylearn2/>`__ which
brings modularity and configurability to Theano where you could create
your neural network through different configuration files so that it
would be easier to experiment different parameters. Arguably, it
provides more modularity by separating the parameters and properties of
neural network to the configuration file.

Decaf
-----

`Decaf <http://caffe.berkeleyvision.org/>`__ is a recently released deep
learning library from UC Berkeley which has state of art neural network
implementations which are tested on the Imagenet classification
competition.

Nolearn
-------

If you want to use excellent Scikit-learn library api in deep learning
as well, \ `Nolearn <http://packages.python.org/nolearn/>`__ wraps Decaf
to make the life easier for you. It is a wrapper on top of Decaf and it
is compatible(mostly) with Scikit-learn, which makes Decaf even more
awesome.

OverFeat
--------

`OverFeat <https://github.com/sermanet/OverFeat>`__ is a recent winner
of \ `Dogs vs Cats (kaggle
competition) <https://plus.google.com/+PierreSermanet/posts/GxZHEH9ynoj>`__ which
is written in C++ but it comes with a Python wrapper as well(along with
Matlab and Lua). It uses GPU through Torch library so it is quite fast.
It also won the detection and localization competition in ImageNet
classification. If your main domain is in computer vision, you may want
to check it out.

Hebel
-----

`Hebel <https://github.com/hannes-brt/hebel>`__ is another neural
network library comes along with GPU support out of the box. You could
determine the properties of your neural networks through YAML
files(similar to Pylearn2) which provides a nice way to separate your
neural network from the code and quickly run your models. Since it has
been recently developed, documentation is lacking in terms of depth and
breadth. It is also limited in terms of neural network models as it only
has one type of neural network model(feed-forward). However, it is
written in pure Python and it will be nice library as it has a lot of
utility functions such as schedulers and monitors which we did not see
any library provides such functionalities.

Neurolab
--------

`NeuroLab <https://code.google.com/p/neurolab/>`__ is another neural
network library which has nice api(similar to Matlab’s api if you are
familiar) It has different variants of Recurrent Neural Network(RNN)
implementation unlike other libraries. If you want to use RNN, this
library might be one of the best choice with its simple API.

Integration with other languages
================================

You do not know any Python but great in another language? Do not
despair! One of the strengths of Python (among many other) is that it is
a perfect glue language that you could use your tool of choice
programming language with these libraries through access from Python.
Following packages for respective programming languages could be used to
combine Python with other programming languages:

Inactive Libraries
------------------

These are the libraries that did not release any updates for more than
one year, we are listing them because some may find it useful, but it is
unlikely that these libraries will be maintained for bug fixes and
especially enhancements in the future:

- R -> RPython
- Matlab -> matpython
- Java -> Jython
- Lua -> Lunatic Python
- Julia -> PyCall.jl


If we are missing one of your favorite packages in Python for machine
learning, feel free to let us know in the comments. We will gladly add
that library to our blog post as well.
