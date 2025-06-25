Guide to installing and running GRAS
====================================

by Sai Krishanth Pulikesi Mannan (saikrishanth@arizona.edu)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

\*This has been tested on a 2021 MacBook Pro running macOS 12.6, a
general install guide is available at
https://spitfire.estec.esa.int/trac/GRAS/wiki/GRAS/GRAS-05-02-01/InstallationGuide

Installing:
-----------

1. Start by installing Geant4 (official installation documentation here:
   https://geant4-userdoc.web.cern.ch/UsersGuides/InstallationGuide/html/index.html):

Software prerequisites:

a. C++ compiler and standard library supporting the C++17 standard. This
   includes gcc 8 or higher on Linux, clang 12 or higher on macOS, and
   visual studio 19 or higher on Windows.
b. cmake (download from the website or brew on macOS)
c. xerces-c (download from the website or brew on macOS)

The latest version is 11.0.3, available at
https://geant4.web.cern.ch/support/download. However, GRAS does not
appear to be compatible with this version on my computer and I found
success running 10.7 instead, available at
https://geant4.web.cern.ch/support/download_archive. Download the gzip
file and untar it. Move the newly untarred file to an appropriate
installation location, henceforth called ``/path/to/geant4.10.07.p04``.
Navigate to ``/path/to/`` and create a new directory called
``geant4.10.07.p04-build`` and change into this directory. Now type:

::

   cmake -DCMAKE_INSTALL_PREFIX=/path/to/geant4.10.07.p04-install -DGEANT4_INSTALL_DATA=ON -DGEANT4_USE_GDML=ON /path/to/geant4.10.07.p04

If successful, you should have an output like
``-- Build files have been written to: /path/to/geant4.10.07.p04-build``.

Now type (N is the number of cores you want to simultaneously use for
the install):

::

   make -jN

After this type:

::

   make install

This will install geant4 on your computer. After this, navigate to
``/path/to/geant4.10.07.p04-install/bin`` and type:

::

   source geant4.sh

2. Now we install GRAS, available from:
   https://essr.esa.int/project/gras-geant4-radiation-analysis-for-space/link/125

First, download the gzip file and untar it. You can then move it to
``/path/to/gras-05-02-01``. Navigate to ``/path/to/`` and make a
directory named ``gras-05-02-01-build`` and change into this directory.
Now type:

::

   cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local/gras/GRAS-05-02-01 -DGRAS_INSTALL_PREFIX=/usr/local/gras/GRAS-05-02-01 -DSTATIC_BUILD=OFF -DWITH_GEANT4_UIVIS=ON -DWITH_MESHING_ANALYSIS=ON -DWITH_ROOT=OFF -DWITH_ZSTR=OFF /path/to/gras-05-02-01

If successful, you should have an output like
``-- Build files have been written to: /path/to/gras-05-02-01-build``.

Now type (N is the number of cores you want to simultaneously use for
the install):

::

   make -jN

After this type (you might have to use sudo, but you can get around that
by setting ``CMAKE_INSTALL_PREFIX = /path/to/gras-05-02-01-install``,
and not including
``-DGRAS_INSTALL_PREFIX=/usr/local/gras/GRAS-05-02-01`` in the above
command):

::

   make install

This will install GRAS on your computer. After this type:

::

   source /usr/local/gras/GRAS-05-02-01/bin/gras-env.sh

3. Some troubleshooting:

You might have the following error while running GRAS:

::

   dyld[53191]: Library not loaded: '@rpath/libG4Tree.dylib'
   Referenced from: '/usr/local/gras/GRAS-05-02-01/bin/gras'
   Reason: tried: '/usr/local/gras/GRAS-05-02-01/lib//libG4Tree.dylib' (no such file), '/usr/local/lib/libG4Tree.dylib' (no such file), '/usr/lib/libG4Tree.dylib' (no such file)
   Abort trap: 6

In which case, navigate to ``/path/to/geant4.10.07.p04-install/lib`` and
copy the lib files present into ``/path/to/gras-05-02-01-install/lib``,
and then type:

::

   export DYLD_LIBRARY_PATH='/path/to/gras-05-02-01-build/lib'

Now GRAS should run.

Using GRAS (coming soon…)
-------------------------

For questions, comments, and suggestions, contact
saikrishanth@arizona.edu
