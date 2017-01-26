FAQ
---

Q:
  Can I use this with vanilla serializers as well as ``ModelSerializer``?
A:
  Sure.  You'll need include the request in the context, to provide access on the querystring:

.. code-block:: python

    MySerializer(obj, context={'request': request})


Q:
  The name ``fields`` conflicts with some other functionality in my API (e.g. `django-filter <https://django-filter.readthedocs.io/en/latest/guide/rest_framework.html>`_).  Can I change it to something else?
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
