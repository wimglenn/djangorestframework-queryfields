from rest_framework.routers import DefaultRouter

from tests.app.views import ExplosiveViewSet
from tests.app.views import QuoteViewSet
from tests.app.views import SnippetViewSet

router = DefaultRouter()
router.register(r'quotes', QuoteViewSet, base_name='api-quote')
router.register(r'snippets', SnippetViewSet, base_name='api-snippet')
router.register(r'explosives', ExplosiveViewSet, base_name='api-explosive')
urlpatterns = router.urls
