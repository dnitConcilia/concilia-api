from .views import TimelineViewSet
from rest_framework.routers import SimpleRouter

app_name = 'timeline'

router = SimpleRouter()

router.register(r'api/timeline', TimelineViewSet)

urlpatterns = []

urlpatterns = urlpatterns + router.urls
