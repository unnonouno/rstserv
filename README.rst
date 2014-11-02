rst server
===========

.. image:: https://travis-ci.org/unnonouno/rstserv.svg?branch=master
   :target: https://travis-ci.org/unnonouno/rstserv

This python script is a simple http server that shows a reStructured text file.

Require
-------

- python (> 2.4)

  - docutils
  - markdown (optional)


Setup
-----

::

 $ pip install rstserv


Usage
-----

::

$ rstserv [-p port] [file]

Run the script with your rst file, and access http://localhost:8080.


Command-line Options
~~~~~~~~~~~~~~~~~~~~

\-p
  port number (default: 8080)

License
-------

This program is distributred under the MIT license.
