# fipy
Python3 version of FiPy (develop), a Finite Volume PDE solver

This is a fork of the development branch (as of 2015/07/26) of FiPy migrated to Python 3.x using 2to3. Please refer to the NIST repo for the official version.

Very little else has been changed besides a bug fix in the matplotlib viewer to ensure it works 
in an IPython notebook (turned off "block"). I also tweaked the legend padding.

This fork is provided as a public repo in case anyone is interested in running a Py3 version and doesn't want to 
bother with 2to3 (although it's a two-line effort). Included here is a build on MacOSX Yosemite.
