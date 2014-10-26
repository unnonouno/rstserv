#!/usr/bin/env python

import glob
from setuptools import setup
from rstserv import __version__

requires = [
    'argparse',
    'docutils',
    ]

setup(
    name='rstserv',
    version=__version__,
    description='Simple reStructured Text Viewer with HTTP Server',
    author='Yuya Unno',
    author_email='unnonouno@gmail.com',
    packages=['rstserv',
              'rstserv.template'],
    package_data={
        'rstserv.template': ['*.css', '*.html']
        },
    scripts=['scripts/rstserv'],
    install_requires=requires,
    )
