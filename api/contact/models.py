import threading

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
		
	def save(self, *args, **kwargs):
		super(Contact, self).save(*args, **kwargs)
		context = {
			'pk': self.id,
			'name': self.name,
			'lastName': self.lastName,
			'email': self.email,
			'subject': self.subject,
			'message': self.message
		}
		t = threading.Thread(target=send_email, args=(context,))
		t.start()
	
def send_email(context):
	template_name = 'contact/get_mail.html'
		
	recipient_list = [
		'conciliaanel@gmail.com',
		'yep.dias@gmail.com'
	]
	try:
		send_email_template(
			'[Concilia] Contato feito pelo site', template_name, context,
			recipient_list, from_email=settings.DEFAULT_FROM_EMAIL,
			fail_silently=False
		)
	except:
		Contact.objects.create(name='Error', lastName='Email',
			email=context['email'], subject='Erro ao enviar o email',
			message='Não foi possível enviar email'
		)
			
	return