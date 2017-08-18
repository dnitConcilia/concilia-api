from .views import NewsViewSet, CategoryNewsViewSet
from rest_framework.routers import SimpleRouter

app_name = 'news'

router = SimpleRouter()

router.register(r'api/news', NewsViewSet)
router.register(r'api/news-category', CategoryNewsViewSet)

urlpatterns = []

urlpatterns = urlpatterns + router.urls
