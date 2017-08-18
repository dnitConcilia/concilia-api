from django.db import models

class CategoryFaq(models.Model):
	name = models.CharField('Nome da categoria', max_length=100)

	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Modificado em', auto_now=True)

	class Meta:
		verbose_name = 'Categoria de perguntas frequentes'
		verbose_name_plural = 'Categorias de perguntas frequentes'
		ordering = ['name']

	def __str__(self):
		return self.name


class Faq(models.Model):
	question = models.CharField('Pergunta', max_length=500, help_text=u"Pergunta que será apresentada no site")
	answer = models.TextField('Resposta', max_length=1000, help_text=u"Resposta para a pergunta que será apresentada no site")
	category = models.ForeignKey('common_questions.CategoryFaq', related_name='perguntas_frequentes', verbose_name='Categoria')

	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Modificado em', auto_now=True)

	class Meta:
		verbose_name = 'Pergunta Frequente'
		verbose_name_plural = 'Perguntas Frequentes'
		ordering = ['question']

	def __str__(self):
		return self.question
