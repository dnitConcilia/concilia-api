from django.db import models

class Photo(models.Model):
	title = models.CharField("Título", max_length=200, blank=True, null=True)
	photo = models.ImageField("Arquivo", upload_to="/gallery/photos")
	legend = models.CharField("Legenda", blank=True, max_length=300)
	credit = models.CharField("Créditos", blank=True, max_length=100)
	link = models.URLField("Link externo", blank=True, null=True)

	created_at  = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at  = models.DateTimeField('Atualizado em', auto_now=True)

	class Meta:
		verbose_name        = "Foto"
		verbose_name_plural = "Fotos"

	def __str__(self):
		return "[{0}] {1}".format(self.credit, self.legend)

class Video(models.Model):
	title = models.CharField("Título", max_length=200)
	description = models.TextField("Descrição", blank=True)
	embed = models.TextField("Código do youtube")

	created_at  = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at  = models.DateTimeField('Atualizado em', auto_now=True)

	class Meta:
		verbose_name        = "Foto"
		verbose_name_plural = "Fotos"

	def __str__(self):
		return "[{0}] {1}".format(self.credit, self.legend)


class CategoryGallery(models.Model):
	category    = models.CharField('Categoria', max_length =100, blank=True, null=True)
	subCategory = models.CharField('Subcategoria', max_length=100, blank=True, null=True)

	created_at  = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at  = models.DateTimeField('Atualizado em', auto_now=True)

	class Meta:
		verbose_name        = "Categoria da notícia"
		verbose_name_plural = "Categorias das notícias"

	def __str__(self):
		return self.name


class Gallery(models.Model):

	title = models.CharField('Título', max_length=500)
	text = models.TextField(verbose_name='Texto', null=True, blank=True)
	categoryGallery = models.ForeignKey('gallery.CategoryGallery', blank=True, null=True)
	slug = models.SlugField('Slug', max_length=500, null=False, blank=False, unique=True, help_text="'slug' é um identificador único que será mostrado na url")
	is_public = models.BooleanField(('É Pública ?'), default=True, blank=True, help_text=('Somente as notícias marcadas como públicas serão apresentadas no site.'))

	photos = models.ManyToManyField('gallery.Photo')
	videos = models.ManyToManyField('gallery.Video')

	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	class Meta:
		verbose_name = 'Notícia'
		verbose_name_plural = 'Notícias'

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if self.slug is None:
			self.slug = slugify(self.categoryGallery.category + self.title)
		super(News, self).save(*args, **kwargs)
