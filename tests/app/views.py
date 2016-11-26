from rest_framework import viewsets
from rest_framework.response import Response

from tests.app.data import get_explosive_list
from tests.app.data import get_explosive_object
from tests.app.data import get_quote_list
from tests.app.data import get_quote_object
from tests.app.data import get_snippet_model_instance
from tests.app.data import get_snippet_queryset
from tests.app.serializers import ExplosiveSerializer
from tests.app.serializers import QuoteSerializer
from tests.app.serializers import SnippetSerializer


class QuoteViewSet(viewsets.ViewSet):

    def list(self, request):
        quotes = get_quote_list()
        serializer = QuoteSerializer(quotes, many=True, context={'request': request})
        response = Response(serializer.data)
        return response

    def retrieve(self, request, pk=None):
        quote = get_quote_object(pk=pk)
        serializer = QuoteSerializer(quote, context={'request': request})
        response = Response(serializer.data)
        return response

    def create(self, request):
        serializer = QuoteSerializer(data={}, context={'request': request})
        response_data = {
            'request_query': request.GET,
            'request_method': request.method,
            'serializer_instance_fields': list(serializer.fields),
        }
        return Response(response_data)


class SnippetViewSet(viewsets.ModelViewSet):

    serializer_class = SnippetSerializer

    def get_queryset(self):
        return get_snippet_queryset()

    def get_object(self):
        pk = self.request.parser_context['kwargs']['pk']
        return get_snippet_model_instance(pk=pk)


class ExplosiveViewSet(viewsets.ViewSet):

    def list(self, request):
        explosives = get_explosive_list()
        serializer = ExplosiveSerializer(explosives, many=True, context={'request': request})
        response = Response(serializer.data)
        return response

    def retrieve(self, request, pk=None):
        explosive = get_explosive_object(pk=pk)
        serializer = ExplosiveSerializer(explosive, context={'request': request})
        response = Response(serializer.data)
        return response
