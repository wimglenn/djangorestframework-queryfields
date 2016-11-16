from rest_framework import serializers

from drf_queryfields import QueryFieldsMixin
from tests.app.fields import BoomField
from tests.app.models import Snippet


class QuoteSerializer(QueryFieldsMixin, serializers.Serializer):

    character = serializers.CharField()
    line = serializers.CharField()
    sketch = serializers.CharField()


class SnippetSerializer(QueryFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = '__all__'


class ExplosiveSerializer(QueryFieldsMixin, serializers.Serializer):

    safe = serializers.CharField()
    boom = BoomField()
