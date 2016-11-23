Quickstart
----------

Specify your base model serializer like this:

.. code-block:: python

    from rest_framework.serializers import ModelSerializer
    from drf_queryfields import QueryFieldsMixin

    class MyModelSerializer(QueryFieldsMixin, ModelSerializer):
        pass


Yeah, that's pretty much it.
