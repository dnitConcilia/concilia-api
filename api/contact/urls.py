from .views import ContactViewSet
from rest_framework.routers import SimpleRouter

app_name = 'contact'

router = SimpleRouter()

router.register(r'api/contact', ContactViewSet)

urlpatterns = []

urlpatterns = urlpatterns + router.urls
