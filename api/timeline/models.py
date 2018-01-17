from django.db import models

class Timeline(models.Model):

	title = models.CharField('Título do evento', max_length=500)
	date = models.DateField('Data do evento', null=False, blank=True)
	text = models.TextField(verbose_name='Texto')
	image = models.ImageField(
		upload_to='timeline/images', verbose_name='Imagem de apresentação',
		null=True, blank=True
	)
	legend_image = models.CharField('Legenda da imagem', max_length=200, null=True, blank=True)

	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	class Meta:
		verbose_name = 'Evento da linha do tempo'
		verbose_name_plural = 'Eventos da linha do tempo'
		ordering = ['-date']

	def __str__(self):
		return self.title

	def has_image(self):
		try:
			if self.image and self.image.size > 0:
				return True
			else:
				return False
		except Exception as err:
			print(u"Não foi possivel verificar o arquivo: ", err)
			return False

	def exists_image_in_path(self):
		if os.path.exists(self.image.path):
			return True
		else:
			return False
