from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.meeting.models import Meeting
from api.meeting.serializers import MeetingReadSerializer, MeetingWriteSerializer


class MeetingViewSet(viewsets.ModelViewSet):
	serializer_class = MeetingReadSerializer
	queryset = Meeting.objects.all()
	permission_classes = (IsAuthenticated,)

	def get_serializer_class(self):
		serializer_class = self.serializer_class

		if self.request.method == 'PUT' or \
			self.request.method == 'PATCH' or \
			self.request.method == 'POST':
			serializer_class = MeetingWriteSerializer

		return serializer_class
