from rest_framework import serializers
from api.communities.models import Community


class CommunityReadSerializer(serializers.ModelSerializer):

	class Meta:
		model   = Community
		exclude = ('created_at', 'updated_at')


class CommunityWriteSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		community, created = Community.objects.get_or_create(**validated_data)
		return community

	class Meta:
		model   = Community
		exclude = ('id', 'created_at', 'updated_at')
