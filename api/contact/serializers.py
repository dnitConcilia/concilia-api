from rest_framework import serializers

from api.contact.models import Contact


class ContactReadSerializer(serializers.ModelSerializer):

	class Meta:
		model   = Contact
		exclude = ('created_at', 'updated_at')


class ContactWriteSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		contact, created = Contact.objects.get_or_create(**validated_data)
		return contact

	class Meta:
		model   = Contact
		exclude = ('id', 'created_at', 'updated_at')
