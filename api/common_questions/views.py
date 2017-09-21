from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.common_questions.models import CategoryFaq, Faq
from api.common_questions.serializers import (
	CategoryFaqReadSerializer, FaqReadSerializer,
	CategoryFaqWriteSerializer,
	FaqWriteSerializer
)


class CategoryFaqViewSet(viewsets.ModelViewSet):
	queryset = CategoryFaq.objects.all()
	serializer_class = CategoryFaqReadSerializer
	permission_classes = (IsAuthenticated,)

	def get_serializer_class(self):
		serializer_class = self.serializer_class

		if self.request.method == 'PUT' or \
			self.request.method == 'PATCH' or \
			self.request.method == 'POST':
			serializer_class = CategoryFaqWriteSerializer

		return serializer_class


class FaqViewSet(viewsets.ModelViewSet):
	queryset = Faq.objects.all().order_by('id')
	serializer_class = FaqReadSerializer
	permission_classes = (IsAuthenticated,)

	def get_serializer_class(self):
		serializer_class = self.serializer_class

		if self.request.method == 'PUT' or \
			self.request.method == 'PATCH' or \
			self.request.method == 'POST':
			serializer_class = FaqWriteSerializer

		return serializer_class
