import re
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db import models
from django.core import validators
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin

SEXO = (
	('0', 'Masculino'),
	('1', 'Feminino'),
	('2', 'Não fornecer'),
)

class User(AbstractBaseUser, PermissionsMixin):
	name        = models.CharField("Nome", max_length=150, blank=True)
	username    = models.CharField(
					"Usuário", max_length=50, unique=True,
					validators=[
						validators.RegexValidator(re.compile('^[\w.@+-]+$'),
						'Informe um nome de usuário válido'
						'Este valor deve conter apenas letras, digitos'
						'e os caracteres: @|.|+|-|_',
						'invalid')
					],
					help_text='Um nome curto e único que será usado para identificá-lo',
				)
	email       = models.EmailField("Email", unique=True)
	birth       = models.DateField("Data de nascimento", blank=True, null=True)
	rg          = models.CharField("Registro geral (RG)", max_length=10, blank=True, null=True)
	cpf         = models.CharField(
					"Código de pessoa fisica (CPF)",
					max_length=15,
					unique=True,
					blank=True, null=True
				)
	sexo        = models.CharField(
					"Sexo",
					max_length=1,
					choices=SEXO,
					blank=True, null=True,
				)
	phone       = models.CharField('Phone', max_length=20, blank=True)

	is_active   = models.BooleanField('Está ativo', default=True)
	is_staff    = models.BooleanField('É da equipe', default=False)
	date_joined = models.DateTimeField(
					'Data de entrada',
					auto_now_add=True
				)

	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def __str__(self):
		return self.name or self.username

	def get_short_name(self):
		return self.name or self.username

	def get_full_name(self):
		return "{0} {1}".format(self.name, self.lastName)

	def save(self, *args, **kwargs):
		if (self.is_staff == True):
			self.profile = 0
			self.is_active = True
		super(User, self).save(*args, **kwargs)

	class Meta:
		verbose_name        = "Usuário"
		verbose_name_plural = "Usuários"
		ordering            = ['name']

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)
