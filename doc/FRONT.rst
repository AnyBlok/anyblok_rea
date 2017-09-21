.. This file is a part of the AnyBlok project
..
..    Copyright (C) 2017 Simon ANDRE <sandre@anybox.fr>
..    Copyright (C) 2017 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
..
.. This Source Code Form is subject to the terms of the Mozilla Public License,
.. v. 2.0. If a copy of the MPL was not distributed with this file,You can
.. obtain one at http://mozilla.org/MPL/2.0/.


.. contents::

Front Matter
============

Information about the AnyBlok / REA project.

Project Homepage
----------------

AnyBlok / REA is hosted on `github <http://github.com>`_ - the main project
page is at http://github.com/AnyBlok/anyblok_rea. Source code is tracked here
using `GIT <https://git-scm.com>`_.

Releases and project status are available on Pypi at 
http://pypi.python.org/pypi/anyblok_rea.

The most recent published version of this documentation should be at
http://rea.anyblok.org.

Project Status
--------------

AnyBlok / Rea is currently in alpha status and is expected to be fairly
stable.   Users should take care to report bugs and missing features on an as-needed
basis.  It should be expected that the development version may be required
for proper implementation of recently repaired issues in between releases;
the latest master is always available at https://github.com/AnyBlok/anyblok_rea/archive/master.zip.

Installation
------------

Install released versions of AnyBlok from the Python package index with 
`pip <http://pypi.python.org/pypi/pip>`_ or a similar tool::

    pip install anyblok_rea

Installation via source distribution is via the ``setup.py`` script::

    python setup.py install

Installation will add the ``anyblok`` commands to the environment.

Unit Test
---------

Run the framework test with ``nose``::

    pip install nose
    nosetests anyblok_rea/tests

Run all the installed bloks::

    anyblok_nose -c config.file.cfg

AnyBlok / rea is tested using `Travis <https://travis-ci.org/AnyBlok/anyblok_rea>`_

REA Pattern
===========

Quote
-----
A lot of docstring is quoted on::

    Model-Driven Design Using Business Patterns
    Authors: Hruby, Pavel
    ISBN-10 3-540-30154-2 Springer Berlin Heidelberg New York
    ISBN-13 978-3-540-30154-7 Springer Berlin Heidelberg New York

External documentation
----------------------
`REA technology <http://reatechnology.com>`_

`Wikipedia REA <http://en.wikipedia.org/wiki/Resources,_events,_agents_%28accounting_model%29>`_

`William E. McCarthy personal web page <https://www.msu.edu/~mccarth4/>`_

`Modeling Business Enterprises as Value-Added Process Hierarchies with Resource-Event-Agent Object Templates <https://www.msu.edu/user/mccarth4/SYOBJCT.htm>`_

`REA mailing list <https://groups.yahoo.com/neo/groups/REATechnology/info>`_

`REA, a semantic model for Internet supply chain collaboration <http://www.jeffsutherland.org/oopsla2000/mccarthy/mccarthy.htm>`_

Contributing (hackers needed!)
------------------------------

Anyblok / REA is at a very early stage, feel free to fork, talk with core dev, and spread the word!

Author
------

Simon ANDRE

Contributors
------------

`Anybox <http://anybox.fr>`_ team:

* Jean-Sébastien Suzanne
* Simon Andre

Bugs
----

Bugs and feature enhancements to AnyBlok should be reported on the `Issue 
tracker <https://bitbucket.org/AnyBlok/anyblok_rea/issues>`_.
