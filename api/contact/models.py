from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from api.contact.mail import send_email_template

class Contact(models.Model):
	name = models.CharField('Nome', max_length=500)
	lastName = models.CharField('Sobrenome', max_length=500)
	email = models.EmailField("Email")
	subject = models.CharField('Assunto', max_length=500)
	message = models.TextField(verbose_name='Mensagem', null=True, blank=True)
	answered = models.BooleanField(verbose_name='Foi respondido?', default=False)

	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	class Meta:
		verbose_name = 'Contato'
		verbose_name_plural = 'Contatos'
		ordering = ['-created_at']

	def __str__(self):
		return self.name


@receiver(post_save, sender=Contact)
def send_email(sender, instance=None, created=False, **kwargs):
	if created:
		template_name = 'contact/get_mail.html'
		context = {
			'pk': instance.pk,
			'name': instance.name,
			'lastName': instance.lastName,
			'email': instance.email,
			'subject': instance.subject,
			'message': instance.message
		}

		recipient_list = [
			'conciliaanel@gmail.com',
		]

		send_email_template(
			'[Concilia] Contato feito pelo site', template_name, context,
			recipient_list, from_email=settings.DEFAULT_FROM_EMAIL,
			fail_silently=False
		)
