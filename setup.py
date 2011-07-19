#!/usr/bin/env python

from distutils.core import setup

setup(
    name="python-bizdatetime",
    version="0.1",
    description="Module for performing simple business day arithmetics",
    long_description=open("README.txt").read(),
    author="Sergiy Kuzmenko",
    author_email="sergiy@kuzmenko.org",
    url="https://bitbucket.org/shelldweller/python-bizdatetime",
    packages=["bizdatetime"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Office/Business :: Scheduling',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)