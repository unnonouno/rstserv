#!/usr/bin/env python

import glob
from distutils.core import setup

setup(
    name='rstserv',
    version='0.1.0',
    description='Simple reStructured Text Viewer with HTTP Server',
    author='Yuya Unno',
    author_email='unnonouno@gmail.com',
    packages=['rstserv',
              'rstserv.template'],
    package_data={
        'rstserv.template': ['*.css',
                             '*.html',]
        },
    scripts=['scripts/rstserv']
    )
