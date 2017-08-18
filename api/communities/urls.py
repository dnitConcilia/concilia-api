from .views import CommunityViewSet
from rest_framework.routers import SimpleRouter

app_name = 'communities'

router = SimpleRouter()

router.register(r'api/community', CommunityViewSet)

urlpatterns = []

urlpatterns = urlpatterns + router.urls
