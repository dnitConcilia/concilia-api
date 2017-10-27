from rest_framework import serializers
from api.alerts.models import Alert


class AlertReadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Alert
		exclude = ('created_at', 'updated_at')


class AlertWriteSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		alert, created = Alert.objects.get_or_create(**validated_data)
		return alert

	class Meta:
		model = Alert
		exclude = ('id', 'created_at', 'updated_at')
