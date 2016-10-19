Django REST Framework QueryFields
=================================

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


Usage
-----

.. code-block:: bash

    GET http://127.0.0.1:8000/snippets/

    HTTP/1.1 200 OK
    ...
    [
      {
        "id": 1,
        "title": "",
        "code": "foo = \"bar\"\n",
        "linenos": false,
        "language": "python",
        "style": "friendly"
      },
      {
        "id": 2,
        "title": "",
        "code": "print \"hello, world\"\n",
        "linenos": false,
        "language": "python",
        "style": "friendly"
      }
    ]


    GET http://127.0.0.1:8000/snippets/?fields=id,code

    HTTP/1.1 200 OK
    ...
    [
      {
        "id": 1,
        "code": "foo = \"bar\"\n",
      },
      {
        "id": 2,
        "code": "print \"hello, world\"\n",
      }
    ]


    GET http://127.0.0.1:8000/snippets/?fields!=code

    HTTP/1.1 200 OK
    ...
    [
      {
        "id": 1,
        "title": "",
        "linenos": false,
        "language": "python",
        "style": "friendly"
      },
      {
        "id": 2,
        "title": "",
        "linenos": false,
        "language": "python",
        "style": "friendly"
      }
    ]


Feedback
--------

For feature requests or bug reports, please `create an issue here <https://github.com/wimglenn/djangorestframework-queryfields/issues>`_.
