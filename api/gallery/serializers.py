from rest_framework import serializers

from api.gallery.models import CategoryGallery, Gallery, Photo, Video
from api.core.utils import slugifyTitle


class PhotoReadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Photo
		exclude = ('created_at', 'updated_at')


class PhotoWriteSerializer(serializers.ModelSerializer):
	photo = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)

	def create(self, validated_data):
		catGallery, created = Photo.objects.get_or_create(**validated_data)
		return catGallery

	class Meta:
		model = Photo
		exclude = ('id', 'created_at', 'updated_at')


class VideoReadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Video
		exclude = ('created_at', 'updated_at')


class VideoWriteSerializer(serializers.ModelSerializer):
	def create(self, validated_data):
		catGallery, created = Video.objects.get_or_create(**validated_data)
		return catGallery

	class Meta:
		model = Video
		exclude = ('id', 'created_at', 'updated_at')


class CategoryGalleryReadSerializer(serializers.ModelSerializer):
	class Meta:
		model = CategoryGallery
		exclude = ('created_at', 'updated_at')


class CategoryGalleryWriteSerializer(serializers.ModelSerializer):
	def create(self, validated_data):
		catGallery, created = CategoryGallery.objects.get_or_create(**validated_data)
		return catGallery

	class Meta:
		model = CategoryGallery
		exclude = ('id', 'created_at', 'updated_at')


class GalleryReadSerializer(serializers.ModelSerializer):
	categoryGallery = CategoryGalleryReadSerializer(many=False)
	photos = PhotoReadSerializer(many=True)
	videos = VideoReadSerializer(many=True)

	class Meta:
		model = Gallery
		exclude = ('created_at', 'updated_at')


class GalleryWriteSerializer(serializers.ModelSerializer):
	id_categoryGallery = serializers.IntegerField(write_only=True, required=False)
	listPhotos = serializers.ListField(
		child=serializers.IntegerField(min_value=0, max_value=99999)
	)
	listVideos = serializers.ListField(
		child=serializers.IntegerField(min_value=0, max_value=99999)
	)

	def create(self, validated_data):
		errors = {
			'fields_error': {},
			'hasError': False
		}
		if 'id_categoryGallery' not in validated_data:
			errors['fields_error']['id_categoryGallery'] = {
				'message': 'O campo de categoria da notícia é obrigatório',
				'type': 'FieldRequired'
			}
			errors['hasError'] = True

		catGallery = None
		try:
			catGallery = CategoryGallery.objects.get(pk=validated_data.pop('id_categoryGallery'))
		except:
			errors['fields_error']['id_categoryGallery'] = {
				'message': 'Não foi encontrada categoria com esse ID',
				'type': 'ObjectDoesNotExist'
			}
			errors['hasError'] = True

		if 'listPhotos' not in validated_data:
			errors['fields_error']['listPhotos'] = {
				'message': 'O campo de lista de fotos é obrigatório',
				'type': 'FieldRequired'
			}
			errors['hasError'] = True

		if 'listVideos' not in validated_data:
			errors['fields_error']['listVideos'] = {
				'message': 'O campo de lista de videos é obrigatório',
				'type': 'FieldRequired'
			}
			errors['hasError'] = True

		if errors['hasError']:
			raise errors

		errors = {
			'fields_error': {},
			'hasError': False
		}
		listPhotos = []
		for id_photo in validated_data.pop('listPhotos'):
			try:
				listPhotos.append(Photo.objects.get(pk=id_photo))
			except:
				errors['hasError'] = True
				errors['fields_error']['listPhotos']['ids'].append(id_photo)
				errors['fields_error']['listPhotos']['message'] = "Não foram encontradas fotos com os ids"

		listVideos = []
		for id_video in validated_data.pop('listVideos'):
			try:
				listVideos.append(Video.objects.get(pk=id_video))
			except:
				errors['hasError'] = True
				errors['fields_error']['listVideos']['ids'].append(id_video)
				errors['fields_error']['listVideos']['message'] = "Não foram encontrados videos com os ids"

		if errors['hasError']:
			raise errors

		slug = slugifyTitle(validated_data.get('title'), catGallery.category)

		gallery, created = Gallery.objects.get_or_create(
			title=validated_data.pop('title'),
			text=validated_data.pop('text'),
			categoryGallery=catGallery,
			is_public=validated_data.pop('is_public')
		)

		for photo in listPhotos:
			gallery.photos.append(photo)

		for video in listVideos:
			gallery.videos.append(video)

		return gallery

	def update(self, instance, validated_data):
		errors = {
			'fields_error': {},
			'hasError': False
		}
		if 'id_categoryGallery' not in validated_data:
			errors['fields_error']['id_categoryGallery'] = {
				'message': 'O campo de categoria da notícia é obrigatório',
				'type': 'FieldRequired'
			}
			errors['hasError'] = True

		catGallery = None
		try:
			catGallery = CategoryGallery.objects.get(pk=validated_data.pop('id_categoryGallery'))
		except:
			errors['fields_error']['id_categoryGallery'] = {
				'message': 'Não foi encontrada categoria com esse ID',
				'type': 'ObjectDoesNotExist'
			}
			errors['hasError'] = True

		if 'listPhotos' not in validated_data:
			errors['fields_error']['listPhotos'] = {
				'message': 'O campo de lista de fotos é obrigatório',
				'type': 'FieldRequired'
			}
			errors['hasError'] = True

		if 'listVideos' not in validated_data:
			errors['fields_error']['listVideos'] = {
				'message': 'O campo de lista de videos é obrigatório',
				'type': 'FieldRequired'
			}
			errors['hasError'] = True

		if errors['hasError']:
			raise errors

		errors = {
			'fields_error': {},
			'hasError': False
		}
		listPhotos = []
		for id_photo in validated_data.pop('listPhotos'):
			try:
				listPhotos.append(Photo.objects.get(pk=id_photo))
			except:
				errors['hasError'] = True
				errors['fields_error']['listPhotos']['ids'].append(id_photo)
				errors['fields_error']['listPhotos']['message'] = "Não foram encontradas fotos com os ids"

		listVideos = []
		for id_video in validated_data.pop('listVideos'):
			try:
				listVideos.append(Video.objects.get(pk=id_video))
			except:
				errors['hasError'] = True
				errors['fields_error']['listVideos']['ids'].append(id_video)
				errors['fields_error']['listVideos']['message'] = "Não foram encontrados videos com os ids"

		if errors['hasError']:
			raise errors

		slug = slugifyTitle(validated_data.get('title'), catGallery.category)

		Gallery.objects.filter(pk=instance.pk).update(
			title=validated_data.pop('title'),
			text=validated_data.pop('text'),
			categoryGallery=catGallery,
			is_public=validated_data.pop('is_public')
		)

		instance.photos.clear()
		for photo in listPhotos:
			instance.photos.append(photo)

		instance.videos.clear()
		for video in listVideos:
			instance.videos.append(video)

		return instance

	class Meta:
		model = Gallery
		exclude = ('id', 'slug', 'categoryGallery', 'photos', 'videos', 'created_at', 'updated_at')
