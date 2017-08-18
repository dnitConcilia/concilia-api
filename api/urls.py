from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

from patches import routers
from rest_framework.authtoken import views as authtoken

from api.accounts.urls import router as routerAccounts
from api.news.urls import router as routerNews
from api.common_questions.urls import router as routerCommonQuestions
from api.meeting.urls import router as routerMeeting
from api.communities.urls import router as routerCommunities
from api.timeline.urls import router as routerTimeline

router = routers.DefaultRouter()
router.extend(routerAccounts)
router.extend(routerNews)
router.extend(routerCommonQuestions)
router.extend(routerMeeting)
router.extend(routerCommunities)
router.extend(routerTimeline)

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^login/', authtoken.obtain_auth_token),
	url(r'^api/', include('api.core.urls', namespace='core')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls
