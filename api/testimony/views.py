import json
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.testimony.models import Testimony
from api.testimony.serializers import TestimonyReadSerializer, TestimonyWriteSerializer


class TestimonyViewSet(viewsets.ModelViewSet):
	serializer_class = TestimonyReadSerializer
	#queryset = Testimony.objects.all()[:5]
	queryset = Testimony.objects.all()
	permission_classes = (IsAuthenticated,)

	def get_serializer_class(self):
		serializer_class = self.serializer_class

		if self.request.method == 'PUT' or \
			self.request.method == 'PATCH' or \
			self.request.method == 'POST':
			serializer_class = TestimonyWriteSerializer

		return serializer_class

class TestimonyLastFiveView(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)

	def list(self, request, *args, **kwargs):
		try:
			last_five = (Testimony.objects.all().order_by('-created_at'))[:5]
			testimony = TestimonyReadSerializer(last_five, many=True)
			return HttpResponse(json.dumps(testimony.data),
				content_type="application/json"
			)
		except:
			return HttpResponse(json.dumps({}),
					content_type="application/json"
				)