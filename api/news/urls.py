from .views import NewsViewSet, CategoryNewsViewSet, PhotoNewsViewSet
from rest_framework.routers import SimpleRouter

app_name = 'news'

router = SimpleRouter()

router.register(r'api/news', NewsViewSet)
router.register(r'api/news-category', CategoryNewsViewSet)
router.register(r'api/news-photo', PhotoNewsViewSet)

urlpatterns = []

urlpatterns = urlpatterns + router.urls
