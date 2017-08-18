from django.conf.urls import url
from api.accounts import views

from api.accounts.views import UserViewSet

from rest_framework.routers import SimpleRouter

app_name = 'accounts'

router = SimpleRouter()

router.register(r'api/usuario', UserViewSet)

urlpatterns = []

urlpatterns += router.urls
