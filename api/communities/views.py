from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.communities.models import Community
from api.communities.serializers import CommunityReadSerializer, CommunityWriteSerializer


class CommunityViewSet(viewsets.ModelViewSet):
	serializer_class = CommunityReadSerializer
	queryset = Community.objects.all()
	permission_classes = (IsAuthenticated,)

	def get_serializer_class(self):
		serializer_class = self.serializer_class

		if self.request.method == 'PUT' or \
			self.request.method == 'PATCH' or \
			self.request.method == 'POST':
			serializer_class = CommunityWriteSerializer

		return serializer_class

class CommunitySlugView(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)

	def list(self, request, *args, **kwargs):
		try:
			news = CommunityReadSerializer(Community.objects.filter(slug=self.kwargs['slug'])[0])
			return HttpResponse(json.dumps(news.data),
				content_type="application/json"
			)
		except:
			return HttpResponse(json.dumps({}),
					content_type="application/json"
				)
