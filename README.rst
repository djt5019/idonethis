iDoneThis CLI Utility
=====================

|Version| |Documentation| |Status| |Coverage| |License| |GPA|

A simple, small, and opinionated Python CLI for interacting with the awesome
iDoneThis service in a way that suits for my workflow.

This CLI allows you to record your grandiose accomplishments of the day did
today as well as see what others on your team did.

You can find more docs on `ReadTheDocs <http://idonethis.readthedocs.org/en/latest/>`_.


Record what you've done
-----------------------

::

  $ idonethis -m 'Holy smoke I did it!' --token 'my-auth-token' --team 'backend'
  Recorded what you've done, keep up the good work!

  $ echo 'Holy smoke I did it!' | idonethis --token 'my-auth-token' --team 'backend'
  Recorded what you've done, keep up the good work!


Or if you're feeling fancy and want to use your ``$EDITOR``

::

  $ idonethis --token 'my-auth-token' --team 'backend'
  Recorded what you've done, keep up the good work!


See what others have done
-------------------------

::

  $ date
  Thu Jun  4 19:10:11 EDT 2015

  $ idonethis summary --token 'my-auth-token' --team 'backend'
  The "backend" team did this on 2015-06-04

  DanT
  ----

  * Made a PR on something
  * Created a little CLI for stuff

  OtherGuy
  --------

  * Fixed all the things


Or if you want to see who was slacking yesterday

::

  $ idonethis summary --date yesterday --token 'my-auth-token' --team 'backend'
  The "backend" team did this on 2015-06-04

  DanT
  ----

  * Thought about doing work, then didn't

  OtherGuy
  --------

  * Planning to fix all the things


Installation
------------

You can install this off of PyPI using PIP.

::

    $ pip install idonethis


.. include:: contributing.rst


Development
-----------

Python 2.7, 3.2, 3.3, 3.4, and Pypy 2.1 are all supported and integrated
against.  To run `detox`_ locally you'll need all the interpreters... or you
can do what I do and throw it over the fence to TravisCI and hope my config
file hasn't broken again.

1. Create a new virtual environment
2. Install development requirements from *requirements.txt*
3. Run tests  ``nosetests``
4. `detox`_ is installed and will run the test suite across all supported python platforms
5. `python setup.py build_sphinx` will generate documentation into *build/sphinx/html*

TL;DR
+++++

::

    $ virtualenv env
    $ ./env/bin/pip install -qr requirements.txt
    $ source env/bin/activate
    (env) $ nosetests
    (env) $ python setup.py build_sphinx
    (env) $ detox


.. include:: ../HISTORY.rst


License
-------

MIT

.. include:: ../LICENSE


.. _detox: https://testrun.org/tox/

.. |Version| image:: https://badge.fury.io/py/idonethis.svg?
   :target: http://badge.fury.io/py/idonethis

.. |Status| image:: https://travis-ci.org/djt5019/idonethis.svg?branch=master
   :target: https://travis-ci.org/djt5019/idonethis

.. |Coverage| image:: https://coveralls.io/repos/djt5019/idonethis/badge.svg
  :target: https://coveralls.io/r/djt5019/idonethis

.. |Downloads| image:: https://pypip.in/d/idonethis/badge.svg?
   :target: https://pypi.python.org/pypi/idonethis

.. |License| image:: http://img.shields.io/:license-mit-blue.svg
   :target: http://doge.mit-license.org

.. |Documentation| image:: https://readthedocs.org/projects/idonethis/badge/?version=latest
   :target: http://idonethis.readthedocs.org/en/latest
   :alt: Documentation Status

.. |GPA| image:: https://codeclimate.com/github/djt5019/idonethis/badges/gpa.svg
   :target: https://codeclimate.com/github/djt5019/idonethis
   :alt: Code Climate
