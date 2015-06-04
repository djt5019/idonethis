idoneit-cli
===========

|Version| |Downloads| |Status| |Coverage| |License|

A simple Python CLI for interacting with iDoneIt.


Installation
------------

::

    pip install idoneit-cli


.. include:: contributing.rst


Development
-----------

1. Create a new virtual environment
2. Install development requirements from *dev-requirements.txt*
3. Run tests  ``nosetests``
4. `detox`_ is installed and will run the test suite across all supported python platforms
5. `python setup.py build_sphinx` will generate documentation into *build/sphinx/html*

TL;DR
+++++

::

    $ virtualenv env
    $ ./env/bin/pip install -qr dev-requirements.txt
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

.. |Version| image:: https://badge.fury.io/py/idoneit-cli.svg?
   :target: http://badge.fury.io/py/idoneit-cli

.. |Status| image:: https://travis-ci.org/djt5019/idoneit-cli.svg?branch=master
   :target: https://travis-ci.org/djt5019/idoneit-cli

.. |Coverage| image:: https://img.shields.io/coveralls/djt5019/idoneit-cli.svg?
   :target: https://coveralls.io/r/djt5019/idoneit-cli

.. |Downloads| image:: https://pypip.in/d/idoneit-cli/badge.svg?
   :target: https://pypi.python.org/pypi/idoneit-cli

.. |License| image:: https://pypip.in/license/idoneit-cli/badge.svg?
   :target: https://idoneit-cli.readthedocs.org
