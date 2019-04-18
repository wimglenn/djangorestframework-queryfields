from rest_framework.routers import DefaultRouter

from tests.app.views import ExplosiveViewSet
from tests.app.views import QuoteViewSet
from tests.app.views import SnippetViewSet

router = DefaultRouter()
router.register(r'quotes', QuoteViewSet, basename='api-quote')
router.register(r'snippets', SnippetViewSet, basename='api-snippet')
router.register(r'explosives', ExplosiveViewSet, basename='api-explosive')
urlpatterns = router.urls
