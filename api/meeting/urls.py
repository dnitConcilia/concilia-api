from .views import MeetingViewSet
from rest_framework.routers import SimpleRouter

app_name = 'meeteing'

router = SimpleRouter()

router.register(r'api/meeting', MeetingViewSet)

urlpatterns = []

urlpatterns = urlpatterns + router.urls
