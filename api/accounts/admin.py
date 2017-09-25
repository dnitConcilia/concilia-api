from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from api.accounts.models import User
from api.accounts.forms import UserAdminCreationForm, UserAdminForm


class UserAdmin(BaseUserAdmin):

	add_form = UserAdminCreationForm
	add_fieldsets = (
		(
			None,
			{
				'fields': ('username', 'email', 'password1', 'password2')
			}
		),
	)
	form = UserAdminForm
	fieldsets = (
		(
			None,
			{
				'fields': ('username', 'email')
			}
		),
		(
			'Informações Básicas',
			{
				'fields': (
					'name', 'birth', 'rg',
					'cpf', 'sexo', 'phone'
				)
			}
		),
		(
			'Permissões',
			{
				'fields': (
					'is_active', 'is_staff', 'is_superuser',
					'groups', 'user_permissions'
				)
			}
		),
	)
	list_display = (
		'name', 'username', 'email',
		'is_active', 'is_staff', 'is_superuser',
		'date_joined',
	)


admin.site.register(User, UserAdmin)
