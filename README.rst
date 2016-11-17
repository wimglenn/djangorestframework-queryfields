Django REST framework QueryFields
=================================

|Travis|_ |Coveralls|_

.. |Travis| image:: https://img.shields.io/travis/wimglenn/djangorestframework-queryfields.svg?branch=master
.. _Travis: https://travis-ci.org/wimglenn/djangorestframework-queryfields

.. |Coveralls| image:: https://coveralls.io/repos/github/wimglenn/djangorestframework-queryfields/badge.svg?branch=master
.. _Coveralls: https://coveralls.io/github/wimglenn/djangorestframework-queryfields?branch=master


Introduction
------------

This library allows API users to specify which fields they're interested in, using query parameters of the request.

- Fewer bytes down the wire = snappier ajax for your webapps
- Decrease backend load when expensive fields go unneeded


Installation
------------

.. code-block:: bash

    pip install djangorestframework-queryfields


Quickstart
----------

Specify your base model serializer like this:

.. code-block:: python

    from rest_framework.serializers import ModelSerializer
    from drf_queryfields import QueryFieldsMixin

    class MyModelSerializer(QueryFieldsMixin, ModelSerializer):
        pass


Yeah, that's pretty much it.


Usage
-----

.. code-block:: bash

    GET http://127.0.0.1:8000/things/

    HTTP/1.1 200 OK
    ...
    [
      {
        "id": 1,
        "key1": "val1",
        "key2": "val2",
        "key3": "val3",
      },
      {
        "id": 2,
        "key1": "valA",
        "key2": "valB",
        "key3": "valC",
      }
    ]


    GET http://127.0.0.1:8000/things/?fields=id,key2

    HTTP/1.1 200 OK
    ...
    [
      {
        "id": 1,
        "key2": "val2",
      },
      {
        "id": 2,
        "key2": "valB",
      }
    ]


    GET http://127.0.0.1:8000/things/?fields!=key2

    HTTP/1.1 200 OK
    ...
    [
      {
        "id": 1,
        "key1": "val1",
        "key3": "val3",
      },
      {
        "id": 2,
        "key1": "valA",
        "key3": "valC",
      }
    ]


FAQ
---

Q:
  Can I use this with vanilla serializers as well as ``ModelSerializer``?
A:
  Sure.  You'll need include the request in the context, to provide access on the querystring:

.. code-block:: python

    MySerializer(obj, context={'request': request})


Q:
  The name ``fields`` conflicts with some other functionality in my API (e.g. `django-filter <https://django-filter.readthedocs.io/en/latest/rest_framework.html>`_).  Can I change it to something else?
A:
  Yep.  Override a couple of attributes on the class, and then Python's `MRO <https://docs.python.org/3/glossary.html#term-method-resolution-order>`_ will take care of the rest.  For example:

.. code-block:: python

    class MyModelSerializer(QueryFieldsMixin, ModelSerializer):

        include_arg_name = 'include'
        exclude_arg_name = 'exclude'
        delimiter = '|'


Now request like ``GET /things/?exclude=key2|key3`` instead of the default ``GET /things/?fields!=key2,key3``.

Q:
  This thing broke, you suck... / Hey, wouldn't it be cool if...
A:
  Well, that's not really a question, pal.  For feature requests or bug reports, please `create an issue here <https://github.com/wimglenn/djangorestframework-queryfields/issues>`_.
