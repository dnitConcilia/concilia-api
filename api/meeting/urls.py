from .views import MeetingViewSet, NoticeTypeViewSet, NoticeViewSet
from rest_framework.routers import SimpleRouter

app_name = 'meeteing'

router = SimpleRouter()

router.register(r'api/meeting', MeetingViewSet)
router.register(r'api/notice-category', NoticeTypeViewSet)
router.register(r'api/notice', NoticeViewSet)

urlpatterns = []

urlpatterns = urlpatterns + router.urls
