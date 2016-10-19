from rest_framework import viewsets
from rest_framework.response import Response

from tests.app.data import get_quote_list, get_quote_object, get_snippet_queryset, get_snippet_model_instance
from tests.app.serializers import QuoteSerializer, SnippetSerializer


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


class SnippetViewSet(viewsets.ModelViewSet):

    serializer_class = SnippetSerializer

    def get_queryset(self):
        return get_snippet_queryset()

    def get_object(self):
        pk = self.request.parser_context['kwargs']['pk']
        return get_snippet_model_instance(pk=pk)
