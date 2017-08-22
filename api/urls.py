from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

from patches import routers
from rest_framework.authtoken import views as authtoken

from api.accounts.urls import router as routerAccounts
from api.news.urls import router as routerNews
from api.news.views import NewsSlugView, NewsLastSixView
from api.common_questions.urls import router as routerCommonQuestions
from api.meeting.urls import router as routerMeeting
from api.communities.urls import router as routerCommunities
from api.timeline.urls import router as routerTimeline
from api.documents.urls import router as routerDocuments

router = routers.DefaultRouter()
router.extend(routerAccounts)
router.extend(routerNews)
router.extend(routerCommonQuestions)
router.extend(routerMeeting)
router.extend(routerCommunities)
router.extend(routerTimeline)
router.extend(routerDocuments)

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^login/', authtoken.obtain_auth_token),
	url(r'^api/news-slug/(?P<slug>[\-\d\w]+)/$', NewsSlugView.as_view({'get': 'list'})),
	url(r'^api/news-last-six/$', NewsLastSixView.as_view({'get': 'list'})),
	url(r'^api/', include('api.core.urls', namespace='core')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls
