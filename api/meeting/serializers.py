from rest_framework import serializers
from api.meeting.models import Meeting, Notice, NoticeType


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


class NoticeTypeReadSerializer(serializers.ModelSerializer):
	class Meta:
		model = NoticeType
		exclude = ('created_at', 'updated_at')


class NoticeTypeWriteSerializer(serializers.ModelSerializer):
	def create(self, validated_data):
		noticeType, created = NoticeType.objects.get_or_create(**validated_data)
		return noticeType

	class Meta:
		model = NoticeType
		exclude = ('id', 'created_at', 'updated_at')


class NoticeReadSerializer(serializers.ModelSerializer):
	noticeType = NoticeTypeReadSerializer()

	class Meta:
		model   = Notice
		exclude = ('created_at', 'updated_at')


class NoticeWriteSerializer(serializers.ModelSerializer):
	notice = serializers.FileField(max_length=None, use_url=True, allow_empty_file=True)

	def create(self, validated_data):
		notice, created = Notice.objects.get_or_create(**validated_data)
		return notice

	class Meta:
		model   = Notice
		exclude = ('id', 'created_at', 'updated_at')
