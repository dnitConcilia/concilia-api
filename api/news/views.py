from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.news.models import CategoryNews, News
from api.news.serializers import (
	CategoryNewsReadSerializer, NewsReadSerializer,
	CategoryNewsWriteSerializer,
	NewsWriteSerializer
)


class CategoryNewsViewSet(viewsets.ModelViewSet):
	queryset = CategoryNews.objects.all()
	serializer_class = CategoryNewsReadSerializer
	permission_classes = (IsAuthenticated,)

	def get_serializer_class(self):
		serializer_class = self.serializer_class

		if self.request.method == 'PUT' or \
			self.request.method == 'PATCH' or \
			self.request.method == 'POST':
			serializer_class = CategoryNewsWriteSerializer

		return serializer_class


class NewsViewSet(viewsets.ModelViewSet):
	queryset = News.objects.all()
	serializer_class = NewsReadSerializer
	permission_classes = (IsAuthenticated,)

	def get_serializer_class(self):
		serializer_class = self.serializer_class

		if self.request.method == 'PUT' or \
			self.request.method == 'PATCH' or \
			self.request.method == 'POST':
			serializer_class = NewsWriteSerializer

		return serializer_class
