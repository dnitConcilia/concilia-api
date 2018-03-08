from rest_framework import serializers
from api.testimony.models import Testimony


class TestimonyReadSerializer(serializers.ModelSerializer):

	class Meta:
		model   = Testimony
		exclude = ('created_at', 'updated_at')


class TestimonyWriteSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		testimony, created = Testimony.objects.get_or_create(**validated_data)
		return testimony

	class Meta:
		model   = Testimony
		exclude = ('id', 'created_at', 'updated_at')
