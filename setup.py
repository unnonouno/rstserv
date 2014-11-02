#!/usr/bin/env python

import os
from setuptools import setup
from rstserv import __version__

requires = [
    'argparse',
    'docutils',
    ]


def read(name):
    return open(os.path.join(os.path.dirname(__file__), name)).read()


setup(
    name='rstserv',
    version=__version__,
    description='Simple reStructured Text Viewer with HTTP Server',
    long_description=read('README.rst'),
    author='Yuya Unno',
    author_email='unnonouno@gmail.com',
    url='https://github.com/unnonouno/rstserv',
    packages=['rstserv',
              'rstserv.template'],
    package_data={
        'rstserv.template': ['*.css', '*.html']
        },
    scripts=['scripts/rstserv'],
    install_requires=requires,
    license='MIT',
    classifiers=[
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Utilities',
    ],
    )
