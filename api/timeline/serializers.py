from rest_framework import serializers
from api.timeline.models import Timeline


class TimelineReadSerializer(serializers.ModelSerializer):

	class Meta:
		model   = Timeline
		exclude = ('created_at', 'updated_at')


class TimelineWriteSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		timeline, created = Timeline.objects.get_or_create(**validated_data)
		return timeline

	class Meta:
		model   = Timeline
		exclude = ('id', 'created_at', 'updated_at')
