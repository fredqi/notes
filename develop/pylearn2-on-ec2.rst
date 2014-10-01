

====================================================
Deep Learning in Python with Pylearn2 and Amazon EC2
====================================================

:URL: http://www.kurtsp.com/deep-learning-in-python-with-pylearn2-and-amazon-ec2.html

Mon 10 February 2014
                    

In working on a Kaggle competition, I wanted to start working with
neural networks. There are a few libraries to do this, but I decided to
use `Pylearn2 <http://deeplearning.net/software/pylearn2/>`__. It's
built to compile your code onto the GPU. My only problem is that, while
I have a beefy 2011 Macbook Pro, it has an AMD card - no cuda. Well,
let's worry about that later.

After checking out the github repo, I moved to ``DIRECTORY``, and
started working through the softmax\_regression tutorial. I've seen
people complain that the documentation for Pylearn2 is mediocre at best.
I've actually found the tutorials at least to be fairly decent thus far
- so maybe that situation has improved. I'm still trying to get used to
their API - it's a good deal more complicated than scikit-learn, for
example.

The softmax\_regression tutorial trains a softmax regressor (a
multi-class logistic regressor) on the well-known MNIST library. It's
straight-forward and runs just fine on my Macbook Pro's CPU. Then I
moved to the multilayer\_perceptron tutorial. This tutorial actually
warns you you'll probably want a GPU.

I set up the multilayer\_perceptron based on the tutorial. And waited..
and waited.. and then went to make some lunch. Then I got back, saw it
still running, and started looking at what Amazon EC2 instances I could
set up. There are two types ``g2.2xlarge`` and ``cg1.4xlarge``. g2
instances are the current generation, have a K104 GPU, are about a
quarter the cost, and are usually used for "Game streaming, 3D
application streaming, and other server-side graphics workloads". cg1
have more CPU compute units, a more powerful M2050 "Fermi" GPU, are more
expensive, and are often used for "Computational chemistry, rendering,
financial modeling, and engineering design".

Let's see how they stack up. I spun up one of each instance using the
Ubuntu 12.04 hvm instance. Two notes: 1. The hvm version is a bit
further down the list than the initially visible paravirtual Ubuntu
option, which cannot be used with GPU compute instances. 2. The old cg1
instances are available on US East and specifically are not available on
US West.

After some debugging, I came up with the following shell script that
sets up the entire environment.

::

    sudo apt-get -y update
    sudo apt-get -y upgrade
    sudo apt-get -y dist-upgrade
    sudo apt-get -y install git make python-dev python-setuptools libblas-dev gfortran g++ python-pip python-numpy python-scipy liblapack-dev
    sudo pip install ipython nose
    sudo apt-get install screen
    sudo pip install --upgrade git+git://github.com/Theano/Theano.git
    wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1204/x86_64/cuda-repo-ubuntu1204_5.5-0_amd64.deb
    sudo dpkg -i cuda-repo-ubuntu1204_5.5-0_amd64.deb
    sudo apt-get update
    sudo apt-get install cuda
    #THEANO_FLAGS=floatX=float32,device=gpu0 python /usr/local/lib/python2.7/dist-packages/theano/misc/check_blas.py
    git clone git://github.com/lisa-lab/pylearn2.git
    cd pylearn2
    sudo python setup.py install
    cd ..
    echo "export PATH=/usr/local/cuda-5.5/bin:$PATH" >> .bashrc
    echo "export LD_LIBRARY_PATH=/usr/local/cuda-5.5/lib64:$LD_LIBRARY_PATH" >> .bashrc
    echo "export PYLEARN2_DATA_PATH=/home/ubuntu/data" >> .bashrc
    source .bashrc  
    mkdir -p data/mnist/
    cd data/mnist/
    wget http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
    gunzip train-images-idx3-ubyte.gz
    wget http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
    gunzip train-labels-idx1-ubyte.gz
    wget http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
    gunzip t10k-images-idx3-ubyte.gz
    wget http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz
    gunzip t10k-labels-idx1-ubyte.gz
    cd ../..
    echo '[global]
    floatX = float32
    device = gpu0

    [nvcc]
    fastmath = True' > .theanorc

This sets up several things.

#. ipython
#. the MNIST data set in ``~/data/mnist``
#. The nvcc cuda compiler, pylearn2, and theano

That does the system-wide setup. Next, I ran ``time python work.py``,
where work.py is the following file.

::

    from __future__ import division
    from pylearn2.train import Train
    from pylearn2.datasets.mnist import MNIST
    from pylearn2.models import softmax_regression, mlp
    from pylearn2.training_algorithms import bgd
    from pylearn2.termination_criteria import MonitorBased
    from pylearn2.train_extensions import best_params
    from pylearn2.utils import serial
    from theano import function
    from theano import tensor as T
    import numpy as np
    import os

    h0 = mlp.Sigmoid(layer_name='h0', dim=500, sparse_init=15)
    ylayer = mlp.Softmax(layer_name='y', n_classes=10, irange=0)
    layers = [h0, ylayer]

    model = mlp.MLP(layers, nvis=784)
    train = MNIST('train', one_hot=1, start=0, stop=50000)
    valid = MNIST('train', one_hot=1, start=50000, stop=60000)
    test = MNIST('test', one_hot=1, start=0, stop=10000)

    monitoring = dict(valid=valid)
    termination = MonitorBased(channel_name="valid_y_misclass")
    extensions = [best_params.MonitorBasedSaveBest(channel_name="valid_y_misclass", 
        save_path="train_best.pkl")]
    algorithm = bgd.BGD(batch_size=10000, line_search_mode = 'exhaustive', conjugate = 1,
            monitoring_dataset = monitoring, termination_criterion = termination)

    save_path = "train_best.pkl"
    if os.path.exists(save_path):
        model = serial.load(save_path)
    else:
        print 'Running training'
        train_job = Train(train, model, algorithm, extensions=extensions, save_path="train.pkl", save_freq=1)
        train_job.main_loop()

    X = model.get_input_space().make_batch_theano()
    Y = model.fprop(X)

    y = T.argmax(Y, axis=1)
    f = function([X], y)
    yhat = f(test.X)

    y = np.where(test.get_targets())[1]

    print 'accuracy', (y==yhat).sum() / y.size

I converted the tutorials from YAML to Python just because I prefer to
understand what I'm doing in the context of Python rather than YAML -
there's a pretty simple 1-to-1 conversion between them. Since
convergence conditions are the same, all computers achieve 0.9813
accuracy. However, the time's are dramatically different.

+---------------+---------------+------------+
| Computer      | Time          | Time (s)   |
+---------------+---------------+------------+
| Macbook Pro   | 118m49.801s   | 7129.801   |
+---------------+---------------+------------+
| g2.2xlarge    | 28m14.577s    | 1694.577   |
+---------------+---------------+------------+
| cg1.4xlarge   | 19m3.275s     | 1143.275   |
+---------------+---------------+------------+

|image0|

Looking at the numbers, a few conclusions:

#. Don't try to use the CPU for tasks that are meant for the GPU. It's
   just really slow.
#. The g2 instances are about 50% slower than the cg1 instances. On the
   other hand, they're about 28% the price. Ergo, g2 is about half the
   price in computing units - they're half as slow but 4 times cheaper.
   That being said, if I were running a small to medium size job, it
   might be worth the 50% time savings.

If anyone has a retina Macbook Pro, those have some fairly beefy GPUs in
them, and I'd be very curious to see how they stack up.

--------------

Please enable JavaScript to view the `comments powered by Disqus. <http://disqus.com/?ref_noscript>`__

.. |image0| image:: http://www.kurtsp.com/img/ec2compare.png
