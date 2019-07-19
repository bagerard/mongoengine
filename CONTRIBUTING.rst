Contributing to MongoEngine
===========================

MongoEngine has a large `community
<https://raw.github.com/MongoEngine/mongoengine/master/AUTHORS>`_ and
contributions are always encouraged. Contributions can be as simple as
minor tweaks to the documentation. Please read these guidelines before
sending a pull request.

Bugfixes and New Features
-------------------------

Before starting to write code, look for existing `tickets
<https://github.com/MongoEngine/mongoengine/issues?state=open>`_ or `create one
<https://github.com/MongoEngine/mongoengine/issues>`_ for your specific
issue or feature request. That way you avoid working on something
that might not be of interest or that has already been addressed. If in doubt
post to the `user group <http://groups.google.com/group/mongoengine-users>`

Supported Interpreters
----------------------

MongoEngine supports CPython 2.7 and newer. Language
features not supported by all interpreters can not be used.

Python 2/3 compatibility
----------------------

The codebase is written in a compatible manner for python 2 & 3 so it
is important that this is taken into account when it comes to discrepencies
between the two versions (see https://python-future.org/compatible_idioms.html).
Travis runs the tests against different Python versions as a safety net.


Style Guide
-----------

MongoEngine uses `black <https://github.com/python/black>`_ for code
formatting.

Testing
-------

All tests are run on `Travis <http://travis-ci.org/MongoEngine/mongoengine>`_
and any pull requests are automatically tested. Any pull requests without
tests will take longer to be integrated and might be refused.

You may also submit a simple failing test as a pull request if you don't know
how to fix it, it will be easier for other people to work on it and it may get
fixed faster.

General Guidelines
------------------

- Avoid backward breaking changes if at all possible.
- If you *have* to introduce a breaking change, make it very clear in your
  pull request's description. Also, describe how users of this package
  should adapt to the breaking change in docs/upgrade.rst.
- Write inline documentation for new classes and methods.
- Write tests and make sure they pass (make sure you have a mongod
  running on the default port, then execute ``python setup.py nosetests``
  from the cmd line to run the test suite).
- Ensure tests pass on all supported Python, PyMongo, and MongoDB versions.
  You can test various Python and PyMongo versions locally by executing
  ``tox``. For different MongoDB versions, you can rely on our automated
  Travis tests.
- Add enhancements or problematic bug fixes to docs/changelog.rst.
- Add yourself to AUTHORS :)

Documentation
-------------

To contribute to the `API documentation
<http://docs.mongoengine.org/en/latest/apireference.html>`_
just make your changes to the inline documentation of the appropriate
`source code <https://github.com/MongoEngine/mongoengine>`_ or `rst file
<https://github.com/MongoEngine/mongoengine/tree/master/docs>`_ in a
branch and submit a `pull request <https://help.github.com/articles/using-pull-requests>`_.
You might also use the github `Edit <https://github.com/blog/844-forking-with-the-edit-button>`_
button.

If you want to test your documentation changes locally, you need to install
the ``sphinx`` and ``sphinx_rtd_theme`` packages. Once these are installed,
go to the ``docs`` directory, run ``make html`` and inspect the updated docs
by running ``open _build/html/index.html``.
