from django.db import models

class CommunityPhoto(models.Model):
	"""Tabela para o relacionamento de 1 vila com várias fotos"""
	name = models.CharField('Nome da foto. Formato: Nome foto - Nome comunidade', max_length=500, blank=True, null=True)
	image = models.ImageField(upload_to='community/images', verbose_name='Imagem para página da comunidade', null=True, blank=True)
	credit = models.CharField('Créditos da imagem', max_length=100, blank=True, null=True)
	caption = models.CharField('Legenda da imagem', max_length=300, blank=True, null=True)

	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	class Meta:
		verbose_name = 'Fotos da comunidade'
		verbose_name_plural = 'Fotos das comunidades'

	def __str__(self):
		return self.caption or self.credit

class Community(models.Model):
	title = models.CharField('Nome da Vila ou Comunidade', max_length=500)
	text = models.TextField(verbose_name='Sobre a comunidade', null=True, blank=True)
	textMap = models.TextField(verbose_name='Resumo da comunidade', null=True, blank=True, help_text="Esse campo deve ser preenchido com o resumo sobre a comunidade e será apresentado no mapa com todas as comunidades")
	image = models.ImageField(upload_to='communities/images', verbose_name='Imagem para o mapa das comunidades', null=True, blank=True)
	credit = models.CharField('Cŕeditos da imagem', max_length=100, blank=True, null=True)
	caption = models.CharField('Legenda da imagem', max_length=300, blank=True, null=True)
	lat = models.CharField('Latitude', max_length=100, blank=True, null=False)
	lng = models.CharField('Longitude', max_length=100, blank=True, null=False)
	slug = models.SlugField('Identificador', max_length=500, null=False, blank=False, unique=True, help_text="'slug' é um identificador único que será mostrado na url")

	photos = models.ManyToManyField('communities.CommunityPhoto', verbose_name='Fotos da comunidade')

	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	class Meta:
		verbose_name = 'Comunidade/Vila'
		verbose_name_plural = 'Comunidades/Vilas'
		ordering = ['title']

	def save(self, *args, **kwargs):
		if self.slug is None:
			self.slug = slugify(self.title)
		super(Community, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

	def get_lat_long(self):
		if self.lat and self.long:
			return {'lat': self.lat, 'lng': self.long}
		else:
			return False
