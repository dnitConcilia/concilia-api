import json
import time
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse

from api.alerts.models import Alert
from api.alerts.serializers import (
	AlertReadSerializer, AlertWriteSerializer
)


class AlertViewSet(viewsets.ModelViewSet):
	serializer_class = AlertReadSerializer
	queryset = Alert.objects.all().order_by('expired_at')
	permission_classes = (IsAuthenticated,)

	def get_serializer_class(self):
		serializer_class = self.serializer_class

		if self.request.method == 'PUT' or \
			self.request.method == 'PATCH' or \
			self.request.method == 'POST':
			serializer_class = AlertWriteSerializer

		return serializer_class
