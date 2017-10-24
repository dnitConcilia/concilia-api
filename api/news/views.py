import json
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse

from api.news.models import CategoryNews, News, PhotoNews
from api.news.serializers import (
	CategoryNewsReadSerializer, NewsReadSerializer,
	CategoryNewsWriteSerializer,
	NewsWriteSerializer, 
	PhotoNewsReadSerializer,
	PhotoNewsWriteSerializer
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
	queryset = News.objects.filter(is_public=True).order_by('-published_at')
	serializer_class = NewsReadSerializer
	permission_classes = (IsAuthenticated,)

	def get_serializer_class(self):
		serializer_class = self.serializer_class

		if self.request.method == 'PUT' or \
			self.request.method == 'PATCH' or \
			self.request.method == 'POST':
			serializer_class = NewsWriteSerializer

		return serializer_class

class PhotoNewsViewSet(viewsets.ModelViewSet):
	queryset = PhotoNews.objects.all().order_by('news')
	serializer_class = PhotoNewsReadSerializer
	permission_classes = (IsAuthenticated,)

	def get_serializer_class(self):
		serializer_class = self.serializer_class

		if self.request.method == 'PUT' or \
			self.request.method == 'PATCH' or \
			self.request.method == 'POST':
			serializer_class = PhotoNewsWriteSerializer

		return serializer_class

class NewsSlugView(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)

	def list(self, request, *args, **kwargs):
		try:
			news = NewsReadSerializer(
				News.objects.filter(
					slug=self.kwargs['slug'],
					is_public=True
				)[0]
			)
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
			last_six = (News.objects.filter(is_public=True).order_by('-published_at'))[:6]
			news = NewsReadSerializer(last_six, many=True)
			return HttpResponse(json.dumps(news.data),
				content_type="application/json"
			)
		except:
			return HttpResponse(json.dumps({}),
					content_type="application/json"
				)
