from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.timeline.models import Testimony
from api.timeline.serializers import TestimonyReadSerializer, TestimonyWriteSerializer


class TestimonyViewSet(viewsets.ModelViewSet):
	serializer_class = TestimonyReadSerializer
	queryset = Testimony.objects.all().order_by('-date')
	permission_classes = (IsAuthenticated,)

	def get_serializer_class(self):
		serializer_class = self.serializer_class

		if self.request.method == 'PUT' or \
			self.request.method == 'PATCH' or \
			self.request.method == 'POST':
			serializer_class = TestimonyWriteSerializer

		return serializer_class
