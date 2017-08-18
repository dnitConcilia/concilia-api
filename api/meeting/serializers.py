from rest_framework import serializers
from api.meeting.models import Meeting


class MeetingReadSerializer(serializers.ModelSerializer):

	class Meta:
		model   = Meeting
		exclude = ('created_at', 'updated_at')


class MeetingWriteSerializer(serializers.ModelSerializer):
	ppt = serializers.FileField(max_length=None, use_url=True, allow_empty_file=True)
	pdf = serializers.FileField(max_length=None, use_url=True, allow_empty_file=True)

	def create(self, validated_data):
		meeting, created = Meeting.objects.get_or_create(**validated_data)
		return meeting

	class Meta:
		model   = Meeting
		exclude = ('id', 'created_at', 'updated_at')
