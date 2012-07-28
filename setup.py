#!/usr/bin/env python2

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='waste',
    version='0.0',

    url='https://github.com/bhuztez/waste',
    description='Waste, A Silly Template Engine',

    classifiers = [
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],

    author='bhuztez',
    author_email='bhuztez@gmail.com',

    packages=[
        'waste',
        'waste.html',
    ],

    test_suite = 'waste.tests.suite',
)

