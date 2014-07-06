

===========================
A quick Cython introduction
===========================

:URL: http://blog.perrygeo.net/2008/04/19/a-quick-cython-introduction/

I love python for its beautiful code and practicality. But it’s not
going to win a `pure speed
race <http://shootout.alioth.debian.org/debian/benchmark.php?test=all&lang=python&lang2=gcc>`__
with most languages. Most people think of speed and ease-of-use as polar
opposites - probably because they remember the pain of writing C.
`Cython <http://www.cython.org/>`__ tries to eliminate that duality and
lets you have python syntax with C data types and functions - the best
of both worlds. Keeping in mind that I’m by no means an expert at this,
here are my notes based on my first real experiment with Cython:

EDIT: Based on some feedback I’ve received there seems to be some
confusion - Cython is for generating *C extensions to Python* not
standalone programs. The whole point is to speed up an existing python
app one function at a time. No rewriting the whole application in C or
Lisp. No `writing C extensions by
hand <http://www.dalkescientific.com/writings/NBN/c_extensions.html>`__.
Just an easy way to get C speed and C data types into your slow python
functions.

--------------

So lets say we want to make this function faster. It is the `“great
circle” calculation <http://mathworld.wolfram.com/GreatCircle.html>`__,
a quick spherical trig problem to calculate distance along the earth’s
surface between two points:

*p1.py*

::

    import math

    def great_circle(lon1,lat1,lon2,lat2):
        radius = 3956 #miles
        x = math.pi/180.0

        a = (90.0-lat1)*(x)
        b = (90.0-lat2)*(x)
        theta = (lon2-lon1)*(x)
        c = math.acos((math.cos(a)*math.cos(b)) +
                      (math.sin(a)*math.sin(b)*math.cos(theta)))
        return radius*c

Lets try it out and `time
it <http://www.diveintopython.org/performance_tuning/timeit.html>`__
over 1/2 million function calls:

::

    import timeit  

    lon1, lat1, lon2, lat2 = -72.345, 34.323, -61.823, 54.826
    num = 500000

    t = timeit.Timer("p1.great_circle(%f,%f,%f,%f)" % (lon1,lat1,lon2,lat2), 
                           "import p1")
    print "Pure python function", t.timeit(num), "sec"

About **2.2 seconds**. Too slow!

Lets try a quick rewrite in Cython and see if that makes a difference:
*c1.pyx*

::

    import math

    def great_circle(float lon1,float lat1,float lon2,float lat2):
        cdef float radius = 3956.0 
        cdef float pi = 3.14159265
        cdef float x = pi/180.0
        cdef float a,b,theta,c

        a = (90.0-lat1)*(x)
        b = (90.0-lat2)*(x)
        theta = (lon2-lon1)*(x)
        c = math.acos((math.cos(a)*math.cos(b)) + (math.sin(a)*math.sin(b)*math.cos(theta)))
        return radius*c

Notice that we still *import math* - cython lets you mix and match
python and C data types to some extent. The conversion is handled
automatically though not without cost. In this example all we’ve done is
define a *python* function, declare its input parameters to be floats,
and declare a static C float data type for all the variables. It still
uses the python math module to do the calcs.

Now we need to convert this to C code and compile the python extension.
The best way to do this is through a `setup.py distutils
script <http://ldots.org/pyrex-guide/2-compiling.html#distutils>`__. But
we’ll do it the `manual
way <http://ldots.org/pyrex-guide/2-compiling.html#gcc>`__ for now to
see what’s happening:

::

    # this will create a c1.c file - the C source code to build a python extension
    cython c1.pyx

    # Compile the object file   
    gcc -c -fPIC -I/usr/include/python2.5/ c1.c

    # Link it into a shared library
    gcc -shared c1.o -o c1.so

Now you should have a c1.so (or .dll) file which can be imported in
python. Lets give it a run:

::

        t = timeit.Timer("c1.great_circle(%f,%f,%f,%f)" % (lon1,lat1,lon2,lat2), 
                         "import c1")
        print "Cython function (still using python math)", t.timeit(num), "sec"

About **1.8 seconds**. Not the kind of speedup we were hoping for but
its a start. The bottleneck must be in the usage of the python math
module. Lets use the C standard library trig functions instead:

*c2.pyx*

::

    cdef extern from "math.h":
        float cosf(float theta)
        float sinf(float theta)
        float acosf(float theta)

    def great_circle(float lon1,float lat1,float lon2,float lat2):
        cdef float radius = 3956.0 
        cdef float pi = 3.14159265
        cdef float x = pi/180.0
        cdef float a,b,theta,c

        a = (90.0-lat1)*(x)
        b = (90.0-lat2)*(x)
        theta = (lon2-lon1)*(x)
        c = acosf((cosf(a)*cosf(b)) + (sinf(a)*sinf(b)*cosf(theta)))
        return radius*c

Instead of importing the math module, we use *cdef extern* which uses
the C function declarations from the specified include header (in this
case math.h from the C standard library). We’ve replaced the calls to
some of the expensive python functions and are ready to build the new
shared library and re-test:

::

        t = timeit.Timer("c2.great_circle(%f,%f,%f,%f)" % (lon1,lat1,lon2,lat2), 
                         "import c2")
        print "Cython function (using trig function from math.h)", t.timeit(num), "sec"

Now that’s a bit more like it. \*\* 0.4 seconds \*\* - a 5x speed
increase over the pure python function. What else can we do to speed
things up? Well c2.great\_circle() is still a python function which
means that calling it incurs the overhead of the python API,
constructing the argument tuple, etc. If we could write it as a pure C
function, we might be able to speed things up a bit.

*c3.pyx*

::

    cdef extern from "math.h":
        float cosf(float theta)
        float sinf(float theta)
        float acosf(float theta)

    cdef float _great_circle(float lon1,float lat1,float lon2,float lat2):
        cdef float radius = 3956.0 
        cdef float pi = 3.14159265
        cdef float x = pi/180.0
        cdef float a,b,theta,c

        a = (90.0-lat1)*(x)
        b = (90.0-lat2)*(x)
        theta = (lon2-lon1)*(x)
        c = acosf((cosf(a)*cosf(b)) + (sinf(a)*sinf(b)*cosf(theta)))
        return radius*c

    def great_circle(float lon1,float lat1,float lon2,float lat2,int num):
        cdef int i
        cdef float x
        for i from 0 < = i < num:
            x = _great_circle(lon1,lat1,lon2,lat2)
        return x

Notice that we still have a python function wrapper (\_def\_) which
takes an extra argument, num. The looping is done inside this function
with ``for i from 0 < = i < num:`` instead of the more pythonic but
slower ``for i in range(num):``. The actual work is done in a C function
(\_cdef\_) which returns float type. This runs in **0.2 seconds** - a
10x speed boost over the original python function.

Just to confirm that we’re doing things optimally, lets write a little
app in pure C and time it:

::

    #include <math .h>
    #include <stdio .h>
    #define NUM 500000

    float great_circle(float lon1, float lat1, float lon2, float lat2){
        float radius = 3956.0;
        float pi = 3.14159265;
        float x = pi/180.0;
        float a,b,theta,c;

        a = (90.0-lat1)*(x);
        b = (90.0-lat2)*(x);
        theta = (lon2-lon1)*(x);
        c = acos((cos(a)*cos(b)) + (sin(a)*sin(b)*cos(theta)));
        return radius*c;
    }

    int main() {
        int i;
        float x;
        for (i=0; i < = NUM; i++) 
            x = great_circle(-72.345, 34.323, -61.823, 54.826);
        printf("%f", x);
    }

Now compile it with ``gcc -lm -o ctest ctest.c`` and test it with
``time ./ctest``\ … about **0.2 seconds as well**. This gives me
confidence that my Cython extension is at least as efficient as my C
code (which probably isn’t saying much as my C skills are weak).

--------------

Some cases will be more or less optimal for cython depending on how much
looping, number-crunching and python-function-calling are slowing you
down. In some cases people have reported 100 to 1000x speed boosts. For
other tasks it might not be so helpful. Before going crazy rewriting
your python code in Cython, keep this in mind:

    “We should forget about small efficiencies, say about 97% of the
    time: premature optimization is the root of all evil.” – Donald
    Knuth

In other words, write your program in python first and see if it works
alright. Most of the time it will… some times it will bog down. Use a
`profiler <http://docs.python.org/lib/module-hotshot.html>`__ to find
the slow functions and re-implement them in cython and you should see a
quick return on investment.

Links:
`WorldMill <http://trac.gispython.org/projects/PCL/wiki/WorldMill>`__ -
a python module by Sean Gillies which uses Cython to provide a fast,
clean python interface to the libgdal library for handling vector
geospatial data.

`Writing Fast Pyrex
code <http://www.sagemath.org:9001/WritingFastPyrexCode>`__ (Pyrex is
the predecessor of Cython with similar goals and syntax)
