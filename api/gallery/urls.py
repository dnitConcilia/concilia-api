from .views import GalleryViewSet, CategoryGalleryViewSet, PhotoViewSet, VideoViewSet
from rest_framework.routers import SimpleRouter

app_name = 'gallery'

router = SimpleRouter()

router.register(r'api/photo', PhotoViewSet)
router.register(r'api/video', VideoViewSet)
router.register(r'api/gallery', GalleryViewSet)
router.register(r'api/gallery-category', CategoryGalleryViewSet)

urlpatterns = []

urlpatterns = urlpatterns + router.urls
