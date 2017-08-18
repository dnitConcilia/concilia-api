from rest_framework import serializers

from api.news.models import CategoryNews, News
from api.accounts.models import User
from api.accounts.serializers import UserReadSerializer


class CategoryNewsReadSerializer(serializers.ModelSerializer):
	class Meta:
		model = CategoryNews
		exclude = ('created_at', 'updated_at')


class CategoryNewsWriteSerializer(serializers.ModelSerializer):
	def create(self, validated_data):
		catNews, created = CategoryNews.objects.get_or_create(**validated_data)
		return catNews

	class Meta:
		model = CategoryNews
		exclude = ('id', 'created_at', 'updated_at')


class NewsReadSerializer(serializers.ModelSerializer):
	categoryNews = CategoryNewsReadSerializer(many=False)
	author = UserReadSerializer(many=False)

	class Meta:
		model = News
		exclude = ('created_at', 'updated_at')


class NewsWriteSerializer(serializers.ModelSerializer):
	id_categoryNews = serializers.IntegerField(write_only=True, required=False)
	id_author = serializers.IntegerField(write_only=True, required=False)
	image = serializers.ImageField(max_length=None, use_url=True, allow_empty_file=True)

	def create(self, validated_data):
		errors = {
			'fields_error': {},
			'hasError': False
		}
		if 'id_categoryNews' not in validated_data:
			errors['fields_error']['id_categoryNews'] = {
				'message': 'O campo de categoria da notícia é obrigatório',
				'type': 'FieldRequired'
			}
			errors['hasError'] = True

		catNews = None
		try:
			catNews = CategoryNews.objects.get(pk=validated_data.pop('id_categoryNews'))
		except Exception as ObjectDoesNotExist:
			errors['fields_error']['id_categoryNews'] = {
				'message': 'Não foi encontrada categoria com esse ID',
				'type': 'ObjectDoesNotExist'
			}
			errors['hasError'] = True

		user = User.objects.get(pk=validated_data.pop('id_author'))
		new, created = News.objects.get_or_create(
			title=validated_data.pop('title'),
			sub_title=validated_data.pop('sub_title'),
			text=validated_data.pop('text'),
			categoryNews=catNews,
			published_at=validated_data.pop('published_at'),
			expired_at=validated_data.pop('expired_at'),
			image=validated_data.pop('image'),
			legend_image=validated_data.pop('legend_image'),
			credits_image=validated_data.pop('credits_image'),
			author=user,
			notice_origin=validated_data.pop('notice_origin'),
			slug=validated_data.pop('slug'),
			is_public=validated_data.pop('is_public')
		)

		return new

	def update(self, instance, validated_data):
		errors = {
			'fields_error': {},
			'hasError': False
		}
		if 'id_categoryNews' not in validated_data:
			errors['fields_error']['id_categoryNews'] = {
				'message': 'O campo de categoria da notícia é obrigatório',
				'type': 'FieldRequired'
			}
			errors['hasError'] = True

		try:
			catNews = CategoryNews.objects.get(pk=validated_data.pop('id_categoryNews'))
		except Exception as ObjectDoesNotExist:
			errors['fields_error']['id_categoryNews'] = {
				'message': 'Não foi encontrada categoria com esse ID',
				'type': 'ObjectDoesNotExist'
			}
			errors['hasError'] = True

		user = User.objects.get(pk=validated_data.pop('id_author'))
		News.objects.filter(pk=instance.pk).update(
			title=validated_data.pop('title'),
			sub_title=validated_data.pop('sub_title'),
			text=validated_data.pop('text'),
			categoryNews=catNews,
			published_at=validated_data.pop('published_at'),
			expired_at=validated_data.pop('expired_at'),
			created_at=validated_data.pop('created_at'),
			updated_at=validated_data.pop('updated_at'),
			image=validated_data.pop('image'),
			legend_image=validated_data.pop('legend_image'),
			credits_image=validated_data.pop('credits_image'),
			author=user,
			notice_origin=validated_data.pop('notice_origin'),
			slug=validated_data.pop('slug'),
			is_public=validated_data.pop('is_public')
		)

		return instance

	class Meta:
		model = News
		exclude = ('id', 'categoryNews', 'image', 'created_at', 'updated_at')
