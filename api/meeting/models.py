from django.db import models

MEETING_TYPE = (
	('conselho-executivo', 'Conselho Executivo'),
	('outro', 'Outros')
)

NOTICE_TYPE = (
	('', ''),
	('', ''),
	('', '')
)


class Meeting(models.Model):
	title = models.CharField('Título da ata de reunião', max_length=500)
	description = models.TextField(verbose_name='Descrição', null=True, blank=True)
	ppt = models.FileField(upload_to='apresentacao_reuniao/%Y/%m/%d/', null=False, blank=False)
	pdf = models.FileField(upload_to='ata_reuniao/%Y/%m/%d/', null=False, blank=False)
	date = models.DateField('Data da Ata de reunião', null=True, blank=True)
	meetingType = models.CharField('Tipo de reuniao', max_length=500, choices=MEETING_TYPE)

	created_at  = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at  = models.DateTimeField('Atualizado em', auto_now=True)

	class Meta:
		verbose_name = 'Ata de Reunião'
		verbose_name_plural = 'Atas de Reuniões'
		ordering = ['-date']

	def __str__(self):
		return self.title

class Notice(models.Model):
	title = models.CharField('Título do edital', max_length=500)
	description = models.TextField(verbose_name='Descrição', null=True, blank=True)
	notice = models.FileField(upload_to='edital/%Y/%m/%d/', null=False, blank=False)
	date = models.DateField('Data do edital', null=True, blank=True)
	noticeType = models.CharField('Tipo de edital', max_length=500, choices=NOTICE_TYPE)

	created_at  = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at  = models.DateTimeField('Atualizado em', auto_now=True)

	class Meta:
		verbose_name = "Edital"
		verbose_name_plural = "Editais"

	def __str__(self):
		return self.title
