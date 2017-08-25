import json
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse

from api.gallery.models import CategoryGallery, Gallery, Photo, Video
from api.gallery.serializers import (
	CategoryGalleryReadSerializer, GalleryReadSerializer,
	CategoryGalleryWriteSerializer,
	GalleryWriteSerializer, VideoWriteSerializer,
	VideoReadSerializer, PhotoWriteSerializer,
	PhotoReadSerializer
)


class VideoViewSet(viewsets.ModelViewSet):
	queryset = Video.objects.all()
	serializer_class = VideoReadSerializer
	permission_classes = (IsAuthenticated,)

	def get_serializer_class(self):
		serializer_class = self.serializer_class

		if self.request.method == 'PUT' or \
			self.request.method == 'PATCH' or \
			self.request.method == 'POST':
			serializer_class = VideoWriteSerializer

		return serializer_class


class PhotoViewSet(viewsets.ModelViewSet):
	queryset = Photo.objects.all()
	serializer_class = PhotoReadSerializer
	permission_classes = (IsAuthenticated,)

	def get_serializer_class(self):
		serializer_class = self.serializer_class

		if self.request.method == 'PUT' or \
			self.request.method == 'PATCH' or \
			self.request.method == 'POST':
			serializer_class = PhotoWriteSerializer

		return serializer_class


class CategoryGalleryViewSet(viewsets.ModelViewSet):
	queryset = CategoryGallery.objects.all()
	serializer_class = CategoryGalleryReadSerializer
	permission_classes = (IsAuthenticated,)

	def get_serializer_class(self):
		serializer_class = self.serializer_class

		if self.request.method == 'PUT' or \
			self.request.method == 'PATCH' or \
			self.request.method == 'POST':
			serializer_class = CategoryGalleryWriteSerializer

		return serializer_class


class GalleryViewSet(viewsets.ModelViewSet):
	queryset = Gallery.objects.all().order_by('-published_at')
	serializer_class = GalleryReadSerializer
	permission_classes = (IsAuthenticated,)

	def get_serializer_class(self):
		serializer_class = self.serializer_class

		if self.request.method == 'PUT' or \
			self.request.method == 'PATCH' or \
			self.request.method == 'POST':
			serializer_class = GalleryWriteSerializer

		return serializer_class

class GallerySlugView(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)

	def list(self, request, *args, **kwargs):
		try:
			news = GalleryReadSerializer(Gallery.objects.filter(slug=self.kwargs['slug'])[0])
			return HttpResponse(json.dumps(news.data),
				content_type="application/json"
			)
		except:
			return HttpResponse(json.dumps({}),
					content_type="application/json"
				)
