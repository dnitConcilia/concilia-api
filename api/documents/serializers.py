from rest_framework import serializers
from api.documents.models import Documents


class DocumentsReadSerializer(serializers.ModelSerializer):

	class Meta:
		model   = Documents
		exclude = ('created_at', 'updated_at')


class DocumentsWriteSerializer(serializers.ModelSerializer):
	document = serializers.FileField(max_length=None, use_url=True, allow_empty_file=True)

	def create(self, validated_data):
		documents, created = Documents.objects.get_or_create(**validated_data)
		return documents

	class Meta:
		model   = Documents
		exclude = ('id', 'created_at', 'updated_at')
