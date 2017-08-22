from django.db import models

class Documents(models.Model):
	name = models.CharField('Nome do documento', max_length=500)
	typeDocument = models.CharField('Tipo do documento', max_length=500)
	description = models.TextField(verbose_name='Descrição', null=True, blank=True)
	document = models.FileField(upload_to='documento/%Y/%m/%d/', null=False, blank=False)
	date = models.DateField('Data do documento', null=True, blank=True)

	created_at  = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at  = models.DateTimeField('Atualizado em', auto_now=True)

	class Meta:
		verbose_name = 'Documento'
		verbose_name_plural = 'Documentos'

	def __str__(self):
		return "{0} - {1}".format(self.name, self.typeDocument)
