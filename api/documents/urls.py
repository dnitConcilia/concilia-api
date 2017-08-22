from .views import DocumentsViewSet
from rest_framework.routers import SimpleRouter

app_name = 'documents'

router = SimpleRouter()

router.register(r'api/documents', DocumentsViewSet)

urlpatterns = []

urlpatterns = urlpatterns + router.urls
