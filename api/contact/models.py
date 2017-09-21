from django.db import models


class Contact(models.Model):
	name = models.CharField('Nome', max_length=500)
	lastName = models.CharField('Sobrenome', max_length=500)
	email = models.EmailField("Email")
	subject = models.CharField('Assunto', max_length=500)
	message = models.TextField(verbose_name='Mensagem', null=True, blank=True)

	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	class Meta:
		verbose_name = 'Contato'
		verbose_name_plural = 'Contatos'
		ordering = ['-created_at']

	def __str__(self):
		return self.name
