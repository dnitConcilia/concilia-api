from django.db import models


class Alert(models.Model):

	title = models.CharField('Título', max_length=500)
	text = models.TextField(verbose_name='Texto', null=True, blank=True)
	image = models.ImageField(upload_to='alert/images', verbose_name='Imagem para o alerta', null=True, blank=True)
	link = models.CharField("Link", null=True, blank=True, max_length=100)

	start_at = models.DateField('Data de início', null=True, blank=True)
	expired_at = models.DateField('Data de expiração', null=True, blank=True)

	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	class Meta:
		verbose_name = 'Alerta'
		verbose_name_plural = 'Alertas'
		ordering = ['-created_at']

	def __str__(self):
		return "[de {0} até {1}] {2}".format(self.start_at, self.expired_at, self.title)
