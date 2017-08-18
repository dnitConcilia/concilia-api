from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.accounts.models import User
from api.accounts.serializers import (
	UserReadSerializer, UserWriteSerializer,
	UserWriteSerializerWithoutPasswordField
)

class UserViewSet(viewsets.ModelViewSet):
	serializer_class = UserReadSerializer
	queryset = User.objects.all()
	permission_classes = (IsAuthenticated,)

	def get_serializer_class(self):
		serializer_class = self.serializer_class

		if self.request.method == 'PUT' or self.request.method == 'PATCH':
			serializer_class = UserWriteSerializerWithoutPasswordField
		elif self.request.method == 'POST':
			serializer_class = UserWriteSerializer
		return serializer_class
