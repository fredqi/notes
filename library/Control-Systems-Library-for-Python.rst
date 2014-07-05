
==================================
Control Systems Library for Python
==================================

:URL: http://www.cds.caltech.edu/~murray/wiki/index.php/Control_Systems_Library_for_Python

Python Control Systems Library (python-control)
===============================================


Announcements
-------------

- The python-control user documentation has been shifted from SourceForge to
  MurrayWiki at Caltech. Developer documentation remains on `SourceForge
  <http://python-control.sf.net>`__.

- Version 0.5a has been released: 

   + `release notes
     <http://sourceforge.net/mailarchive/message.php?msg_id=27912588>`__
   + `file download <http://sourceforge.net/projects/python-control/files/>`__


The Python Control Systems Library, python-control, is a python package
that implements basic operations for analysis and design of feedback
control systems.

Project Overview
================

The python-control package is a set of python classes and functions that
implement common operations for the analysis and design of feedback
control systems. The initial goal is to implement all of the
functionality required to work through the examples in the textbook
`Feedback Systems <http://www.cds.caltech.edu/~murray/amwiki>`__ by
Åström and Murray. A MATLAB compatibility package (control.matlab) is
available that provides functions corresponding to the commands
available in the MATLAB Control Systems Toolbox.

Here are some of the basic functions that are (or will be) available in
the package:

-  Linear input/output systems in state space and frequency domain
   (transfer functions)
-  Block diagram algebra: serial, parallel and feedback interconnections
-  Time response: initial, step, impulse (using the scipy.signal
   package)
-  Frequency response: Bode and Nyquist plots
-  Control analysis: stability, reachability, observability, stability
   margins
-  Control design: eigenvalue placement, linear quadratic regulator
-  Estimator design: linear quadratic estimator (Kalman filter)

