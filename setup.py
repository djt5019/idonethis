#!/usr/bin/env python
import codecs

from setuptools import setup

import idonethis

setup(
    name='idonethis',
    description='A simple Python CLI for interacting with idonethis',
    version=idonethis.__version__,
    py_modules=['idonethis'],
    test_suite='nose.collector',
    include_package_data=True,
    long_description=codecs.open('README.rst', encoding='utf-8').read(),
    install_requires=['requests>=2.6.2,<3.0.0'],
    author='Dan Tracy.',
    author_email='djt5019@gmail.com',
    url='https://github.com/djt5019/idonethis',
    entry_points={'console_scripts': ['idonethis=idonethis:main']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
    ],
)
