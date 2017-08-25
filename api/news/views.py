import json
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse

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
	queryset = News.objects.all().order_by('-published_at')
	serializer_class = NewsReadSerializer
	permission_classes = (IsAuthenticated,)

	def get_serializer_class(self):
		serializer_class = self.serializer_class

		if self.request.method == 'PUT' or \
			self.request.method == 'PATCH' or \
			self.request.method == 'POST':
			serializer_class = NewsWriteSerializer

		return serializer_class

class NewsSlugView(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)

	def list(self, request, *args, **kwargs):
		try:
			news = NewsReadSerializer(News.objects.filter(slug=self.kwargs['slug'])[0])
			return HttpResponse(json.dumps(news.data),
				content_type="application/json"
			)
		except:
			return HttpResponse(json.dumps({}),
					content_type="application/json"
				)

class NewsLastSixView(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)

	def list(self, request, *args, **kwargs):
		try:
			last_ten = News.objects.all().order_by('-published_at')[:6]
			last_ten_in_ascending_order = reversed(last_ten)
			news = NewsReadSerializer(last_ten_in_ascending_order, many=True)
			return HttpResponse(json.dumps(news.data),
				content_type="application/json"
			)
		except:
			return HttpResponse(json.dumps({}),
					content_type="application/json"
				)
