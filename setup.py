#!/usr/bin/env python

import glob
from distutils.core import setup

setup(
    name='restserv',
    version='0.1.0',
    description='Simple reStructured Text Viewer with HTTP Server',
    author='Yuya Unno',
    author_email='unnonouno@gmail.com',
    packages=['restserv',
              'restserv.template'],
    package_data={
        'restserv.template': ['*.css',
                              '*.html',]
        },
    scripts=['command/restserv']
    )
