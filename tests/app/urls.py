from rest_framework.routers import DefaultRouter

from tests.app.views import QuoteViewSet, SnippetViewSet


router = DefaultRouter()
router.register(r'quotes', QuoteViewSet, base_name='api-quote')
router.register(r'snippets', SnippetViewSet, base_name='api-snippet')
urlpatterns = router.urls
