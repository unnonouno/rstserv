rest server
===========

This python script is a simple http server that shows a reStructured text file.

Require
-------

- python (> 2.4)

  - docutils
  - markdown


Setup
-----

::

 $ ./setup.py install


Usage
-----

::

$ restserv [-p port] [file]

Run the script with your rest file, and access http://localhost:8080.


Command-line Options
~~~~~~~~~~~~~~~~~~~~

\-p
  port number (default: 8080)

License
-------

This program is distributred under the new BSD license.
