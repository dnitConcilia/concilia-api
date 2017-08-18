from .views import FaqViewSet, CategoryFaqViewSet
from rest_framework.routers import SimpleRouter

app_name = 'common_questions'

router = SimpleRouter()

router.register(r'api/faq', FaqViewSet)
router.register(r'api/faq-category', CategoryFaqViewSet)

urlpatterns = []

urlpatterns = urlpatterns + router.urls
