from django.db import models

class Testimony(models.Model):

	name = models.CharField('Nome da pessoa', max_length=500)
	testimony = models.TextField(verbose_name='Depoimento')
	image = models.ImageField(
		upload_to='testimony/images', verbose_name='Imagem de depoimento',
		null=True, blank=True
	)
	legend_image = models.CharField('Legenda da imagem', max_length=200, null=True, blank=True)
	exPlace = models.CharField('Local onde morava', max_length=500)
	place = models.CharField('Moradia atual', max_length=500)

	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	class Meta:
		verbose_name = 'Depoimento'
		verbose_name_plural = 'Depoimentos'

	def __str__(self):
		return self.name

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
