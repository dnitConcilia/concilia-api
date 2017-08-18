import re

from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers
from api.accounts.models import User


class UserReadSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = (
			'id', 'username', 'name',
			'email', 'sexo', 'cpf', 'phone', 'rg', 'birth'
		)
		read_only_fields = (
			'is_staff', 'is_superuser',
			'is_active', 'date_joined',
		)

class UserWriteSerializer(serializers.ModelSerializer):
	username = serializers.CharField()
	email    = serializers.EmailField()

	def validate_username(self, value):
		users = User.objects.filter(username=value)
		if users:
			user_pk = self.context['request']._stream.path.split('/')[2]
			model = self.context['request']._stream.path.split('/')[1]
			if model == 'user':
				user = User.objects.get(pk=int(user_pk))
				if user.username == users[0].username:
					return value
				else:
					raise serializers.ValidationError("Usuário com este Nome de Usuário já existe.")

		return value

	def validate_email(self, value):
		match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', value)
		if match is None:
			raise serializers.ValidationError("Email incorreto.")

		users = User.objects.filter(email=value)

		if users:
			user_pk = self.context['request']._stream.path.split('/')[2]
			model = self.context['request']._stream.path.split('/')[1]
			if model == 'user':
				user = User.objects.get(pk=int(user_pk))
				if user.username != users[0].username:
					raise serializers.ValidationError("Usuário com este Email já existe.")
				else:
					return value
		return value

	def create(self, validated_data):
		user, created = User.objects.get_or_create(**validated_data)
		return user

	class Meta:
		model = User
		fields = (
			'username', 'name', 'password',
			'email', 'sexo', 'cpf', 'phone', 'rg', 'birth'
		)
		read_only_fields = (
			'is_staff', 'is_superuser',
			'is_active', 'date_joined',
		)

class UserWriteSerializerWithoutPasswordField(serializers.ModelSerializer):
	username      = serializers.CharField()
	email         = serializers.EmailField()

	def validate_username(self, value):
		users = User.objects.filter(username=value)
		if users:
			user_pk = self.context['request']._stream.path.split('/')[2]
			model = self.context['request']._stream.path.split('/')[1]
			if model == 'user':
				user = User.objects.get(pk=int(user_pk))
				if user.username == users[0].username:
					return value
				else:
					raise serializers.ValidationError("Usuário com este Nome de Usuário já existe.")

		return value

	def validate_email(self, value):
		match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', value)
		if match is None:
			raise serializers.ValidationError("Email incorreto.")

		users = User.objects.filter(email=value)

		if users:
			user_pk = self.context['request']._stream.path.split('/')[2]
			model = self.context['request']._stream.path.split('/')[1]
			if model == 'user':
				user = User.objects.get(pk=int(user_pk))
				if user.username != users[0].username:
					raise serializers.ValidationError("Usuário com este Email já existe.")
				else:
					return value
		return value

	def update(self, instance, validated_data):
		User.objects.filter(pk=instance.pk).update(**validated_data)
		return instance

	class Meta:
		model = User
		fields = (
			'username', 'name',
			'email', 'sexo', 'cpf', 'phone',
			'rg', 'birth'
		)
		read_only_fields = (
			'is_staff', 'is_superuser',
			'is_active', 'date_joined',
		)
		extra_kwargs = {
			'email': {
				'validators': []
			},
			'username': {
				'validators': [UnicodeUsernameValidator()]
			}
		}
