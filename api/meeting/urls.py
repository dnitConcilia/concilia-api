from .views import MeetingViewSet
from rest_framework.routers import SimpleRouter

app_name = 'meeteing'

router = SimpleRouter()

router.register(r'api/meeteing', MeetingViewSet)

urlpatterns = []

urlpatterns = urlpatterns + router.urls
