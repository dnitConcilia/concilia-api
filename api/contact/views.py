import json
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse

from api.contact.models import Contact
from api.contact.serializers import (
	ContactReadSerializer, ContactWriteSerializer
)


class ContactViewSet(viewsets.ModelViewSet):
	queryset = Contact.objects.all().order_by('-created_at')
	serializer_class = ContactReadSerializer
	permission_classes = (IsAuthenticated,)

	def get_serializer_class(self):
		serializer_class = self.serializer_class

		if self.request.method == 'PUT' or \
			self.request.method == 'PATCH' or \
			self.request.method == 'POST':
			serializer_class = ContactWriteSerializer

		return serializer_class
