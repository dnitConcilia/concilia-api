from .views import AlertViewSet
from rest_framework.routers import SimpleRouter

app_name = 'alerts'

router = SimpleRouter()

router.register(r'api/alert', AlertViewSet)

urlpatterns = []

urlpatterns = urlpatterns + router.urls
