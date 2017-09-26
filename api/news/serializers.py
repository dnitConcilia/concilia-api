from rest_framework import serializers

from api.news.models import CategoryNews, News
from api.accounts.models import User
from api.accounts.serializers import UserReadSerializer
from api.core.utils import slugifyTitle


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
	# image = serializers.ImageField(required=False, max_length=None, allow_empty_file=True, use_url=True)

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

		if errors['hasError']:
			raise errors

		slug = ''
		published_at = validated_data.pop('published_at')
		if published_at:
			slug = slugifyTitle(validated_data.get('title'), published_at)
		else:
			slug = slugifyTitle(validated_data.get('title'))
		user = User.objects.get(pk=validated_data.pop('id_author'))
		new, created = News.objects.get_or_create(
			title=validated_data.pop('title'),
			subTitle=validated_data.pop('subTitle'),
			text=validated_data.pop('text'),
			categoryNews=catNews,
			published_at=validated_data.pop('published_at'),
			expired_at=validated_data.pop('expired_at'),
			legendImage=validated_data.pop('legendImage'),
			creditsImage=validated_data.pop('creditsImage'),
			slug=slug,
			authorText=validated_data.pop('authorText'),
			author=user,
			noticeOrigin=validated_data.pop('noticeOrigin'),
			is_public=validated_data.pop('is_public')
		)
		if validated_data.get('image'):
			new.image = validated_data.pop('image')
		new.save()
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

		slug = ''
		published_at = validated_data.pop('published_at')
		if published_at:
			slug = slugifyTitle(validated_data.get('title'), published_at)
		else:
			slug = slugifyTitle(validated_data.get('title'))

		user = User.objects.get(pk=validated_data.pop('id_author'))
		News.objects.filter(pk=instance.pk).update(
			title=validated_data.pop('title'),
			subTitle=validated_data.pop('subTitle'),
			text=validated_data.pop('text'),
			categoryNews=catNews,
			published_at=validated_data.pop('published_at'),
			expired_at=validated_data.pop('expired_at'),
			legendImage=validated_data.pop('legendImage'),
			creditsImage=validated_data.pop('creditsImage'),
			slug=slug,
			authorText=validated_data.pop('authorText'),
			author=user,
			noticeOrigin=validated_data.pop('noticeOrigin'),
			is_public=validated_data.pop('is_public')
		)
		if validated_data.get('image'):
			instance.image = validated_data.pop('image')
		instance.save()
		return instance

	class Meta:
		model = News
		exclude = ('id', 'slug', 'categoryNews', 'created_at', 'updated_at')
