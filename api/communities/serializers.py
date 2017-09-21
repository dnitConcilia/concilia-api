from rest_framework import serializers
from api.communities.models import CommunityPhoto, Community


class CommunityPhotoReadSerializer(serializers.ModelSerializer):

	class Meta:
		model   = CommunityPhoto
		exclude = ('created_at', 'updated_at')


class CommunityPhotoWriteSerializer(serializers.ModelSerializer):
	id_community = serializers.IntegerField(max_value=None, min_value=0)

	def create(self, validated_data):
		errors = {
			'fields_error': {},
			'hasError': False
		}
		if 'id_community' not in validated_data:
			errors['fields_error']['id_community'] = {
				'message': 'O campo de comunidade é obrigatório',
				'type': 'FieldRequired'
			}
			errors['hasError'] = True

		community = None
		try:
			community = Community.objects.get(pk=validated_data.pop('id_community'))
		except Exception as ObjectDoesNotExist:
			errors['fields_error']['id_community'] = {
				'message': 'Não foi encontrada comunidade com esse ID',
				'type': 'ObjectDoesNotExist'
			}
			errors['hasError'] = True

		if errors['hasError']:
			raise errors

		community_photo, created = CommunityPhoto.objects.get_or_create(**validated_data)
		community.photos.add(community_photo)

		return community_photo

	class Meta:
		model   = CommunityPhoto
		exclude = ('id', 'created_at', 'updated_at')


class CommunityReadSerializer(serializers.ModelSerializer):
	photos = CommunityPhotoReadSerializer(many=True)

	class Meta:
		model   = Community
		exclude = ('created_at', 'updated_at')


class CommunityWriteSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		community, created = Community.objects.get_or_create(**validated_data)
		return community

	class Meta:
		model   = Community
		exclude = ('id', 'photos', 'created_at', 'updated_at')
