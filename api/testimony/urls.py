from .views import TestimonyViewSet
from rest_framework.routers import SimpleRouter

app_name = 'testimony'

router = SimpleRouter()

router.register(r'api/testimony', TestimonyViewSet)

urlpatterns = []

urlpatterns = urlpatterns + router.urls
