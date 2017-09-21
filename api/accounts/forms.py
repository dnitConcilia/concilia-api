# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = (
			'username', 'email', 'name',
			'birth', 'rg', 'cpf', 'sexo',
			'phone'
		)


class UserAdminCreationForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['username', 'email']


class UserAdminForm(forms.ModelForm):
	class Meta:
		model = User
		fields = (
			'username', 'email', 'name',
			'birth', 'rg', 'cpf', 'sexo',
			'phone', 'is_active', 'is_staff',
		)
