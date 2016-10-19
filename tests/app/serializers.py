from rest_framework import serializers

from drf_queryfields import QueryFieldsMixin
from tests.app.models import Snippet


class QuoteSerializer(QueryFieldsMixin, serializers.Serializer):

    character = serializers.CharField()
    line = serializers.CharField()
    sketch = serializers.CharField()


class SnippetSerializer(QueryFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Snippet
