from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.timeline.models import Timeline
from api.timeline.serializers import TimelineReadSerializer, TimelineWriteSerializer


class TimelineViewSet(viewsets.ModelViewSet):
	serializer_class = TimelineReadSerializer
	queryset = Timeline.objects.all().order_by('-date')
	permission_classes = (IsAuthenticated,)

	def get_serializer_class(self):
		serializer_class = self.serializer_class

		if self.request.method == 'PUT' or \
			self.request.method == 'PATCH' or \
			self.request.method == 'POST':
			serializer_class = TimelineWriteSerializer

		return serializer_class
