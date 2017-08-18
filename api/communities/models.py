from django.db import models

class Community(models.Model):
	title = models.CharField('Nome da Vila ou Comunidade', max_length=500)
	text = models.TextField(verbose_name='Sobre a comunidade', null=True, blank=True)
	lat = models.CharField('Latitude', max_length=100, blank=True, null=False)
	lng = models.CharField('Longitude', max_length=100, blank=True, null=False)
	slug = models.SlugField('Identificador', max_length=500, null=False, blank=False, unique=True, help_text="'slug' é um identificador único que será mostrado na url")

	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	class Meta:
		verbose_name = 'Comunidade/Vila'
		verbose_name_plural = 'Comunidades/Vilas'
		ordering = ['title']

	def save(self, *args, **kwargs):
		if self.slug is None:
			self.slug = slugify(self.title)
		super(Comunidade, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

	def get_lat_long(self):
		if self.lat and self.long:
			return {'lat': self.lat, 'lng': self.long}
		else:
			return False
