from django.db import models

class CategoryNews(models.Model):
	category    = models.CharField('Categoria', max_length =100, blank=True, null=True)
	subCategory = models.CharField('Subcategoria', max_length=100, blank=True, null=True)

	created_at  = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at  = models.DateTimeField('Atualizado em', auto_now=True)

	class Meta:
		verbose_name        = "Categoria da notícia"
		verbose_name_plural = "Categorias das notícias"

	def __str__(self):
		return self.category


class News(models.Model):

	title = models.CharField('Título', max_length=500)
	subTitle = models.CharField('Subtítulo', max_length=500, null=True, blank=True)
	text = models.TextField(verbose_name='Texto', null=True, blank=True)
	categoryNews = models.ForeignKey('news.CategoryNews', blank=True, null=True)
	published_at = models.DateField('Data de publicação', null=False, blank=False)
	image = models.ImageField(upload_to='news/images', verbose_name='Imagem de capa para a Notícia', null=True, blank=True)
	legendImage = models.CharField('Legenda da Imagem', max_length=200, null=True, blank=True)
	creditsImage = models.CharField('Creditos da imagem', max_length=200, null=True, blank=True)
	author = models.ForeignKey('accounts.User', verbose_name='Criado por', editable=False)
	noticeOrigin = models.CharField('Fonte da notícia', max_length=200, null=True, blank=True)
	slug = models.SlugField('Identificador', max_length=500, null=False, blank=False, unique=True, help_text="'slug' é um identificador único que será mostrado na url")
	is_public = models.BooleanField(('É Pública ?'), default=True, blank=True, help_text=('Somente as notícias marcadas como públicas serão apresentadas no site.'))

	expired_at = models.DateField('Data de expiração da notícia', null=True, blank=True)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	class Meta:
		verbose_name = 'Notícia'
		verbose_name_plural = 'Notícias'
		ordering = ['-published_at', 'legendImage']

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if self.slug is None:
			self.slug = slugify(self.title)
		super(News, self).save(*args, **kwargs)

	def has_image(self):
		try:
			if self.image and self.image.size > 0:
				return True
			else:
				return False
		except Exception as err:
			print("Não foi possivel verificar o arquivo: ", err)
			return False

	def exists_image_in_path(self):
		if os.path.exists(self.image.path):
			return True
		else:
			return False
