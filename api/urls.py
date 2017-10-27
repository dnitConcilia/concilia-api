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
from api.documents.urls import router as routerDocuments
from api.gallery.urls import router as routerGallery
from api.contact.urls import router as routerContact
from api.alerts.urls import router as routerAlert

from api.news.views import NewsSlugView, NewsLastSixView
from api.communities.views import CommunitySlugView
from api.gallery.views import GallerySlugView
from api.meeting.views import MeetingCategoryView, NoticeCategoryView

from api.news.views import NewsSlugView, NewsLastSixView

from api.news.views import NewsSlugView, NewsLastSixView

router = routers.DefaultRouter()

router.extend(routerAccounts)
router.extend(routerNews)
router.extend(routerCommonQuestions)
router.extend(routerMeeting)
router.extend(routerCommunities)
router.extend(routerTimeline)
router.extend(routerDocuments)
router.extend(routerGallery)
router.extend(routerContact)
router.extend(routerAlert)

urlpatterns = [
	url(r'^jet/', include('jet.urls', 'jet')),
	url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS

	url(r'^admin/', admin.site.urls),
	url(r'^login/', authtoken.obtain_auth_token),

	url(r'^api/', include('api.core.urls', namespace='core')),

	url(r'^api/meeting-category/(?P<meetingType>[\-\d\w]+)/$', MeetingCategoryView.as_view({'get': 'list'})),

	url(r'^api/notice-category/(?P<noticeType>[\-\d\w]+)/$', NoticeCategoryView.as_view({'get': 'list'})),

	url(r'^api/news-slug/(?P<slug>[\-\d\w]+)/$', NewsSlugView.as_view({'get': 'list'})),
	url(r'^api/news-last-six/$', NewsLastSixView.as_view({'get': 'list'})),

	url(r'^api/community-slug/(?P<slug>[\-\d\w]+)/$', CommunitySlugView.as_view({'get': 'list'})),

	url(r'^api/gallery-slug/(?P<slug>[\-\d\w]+)/$', GallerySlugView.as_view({'get': 'list'})),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls
