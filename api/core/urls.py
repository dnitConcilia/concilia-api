from django.conf.urls import url
from api.core.views import LogoutChangeToken, ConfigSystemView

from rest_framework.routers import SimpleRouter

app_name = 'core'

router = SimpleRouter()

urlpatterns = [
	url(r'^configure/$', ConfigSystemView.as_view({'get': 'list'})),
	url(r'^logout/$', LogoutChangeToken.as_view({'get': 'list'})),
]

urlpatterns = urlpatterns + router.urls
