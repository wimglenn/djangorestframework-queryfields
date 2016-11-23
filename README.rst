Django REST framework QueryFields
=================================

|travis|_ |coveralls|_ |pypi|_ |womm|_

.. |travis| image:: https://img.shields.io/travis/wimglenn/djangorestframework-queryfields.svg?branch=master
.. _travis: https://travis-ci.org/wimglenn/djangorestframework-queryfields

.. |coveralls| image:: https://img.shields.io/coveralls/wimglenn/djangorestframework-queryfields.svg
.. _coveralls: https://coveralls.io/github/wimglenn/djangorestframework-queryfields?branch=master

.. |pypi| image:: https://img.shields.io/pypi/v/djangorestframework-queryfields.svg
.. _pypi: https://pypi.python.org/pypi/djangorestframework-queryfields

.. |womm| image:: https://cdn.rawgit.com/nikku/works-on-my-machine/v0.2.0/badge.svg
.. _womm: https://github.com/nikku/works-on-my-machine

Allows clients to control which fields will be sent in the API response.  Fields are specified in the query, e.g.

.. code-block:: 

    # You want a list of users but you're just interested in the fields "id" and "username":
    GET /users/?fields=id,username

    # You want to see every field except "id" for the specific user tom:
    GET /users/tom/?fields!=id


Documentation is hosted on `Read The Docs <http://djangorestframework-queryfields.readthedocs.io/>`_.
