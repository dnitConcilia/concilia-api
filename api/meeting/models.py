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


class NoticeType(models.Model):
	name = models.CharField('Tipo de edital', max_length=100)

	created_at  = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at  = models.DateTimeField('Atualizado em', auto_now=True)

	class Meta:
		verbose_name = "Tipo de edital"
		verbose_name_plural = "Tipos de editais"

	def __str__(self):
		return self.name

class Notice(models.Model):
	title = models.CharField('Título do edital', max_length=500)
	description = models.TextField(verbose_name='Descrição', null=True, blank=True)
	notice = models.FileField(upload_to='edital/%Y/%m/%d/', verbose_name='Arquivo', null=False, blank=False)
	date = models.DateField('Data do edital', null=True, blank=True)
	noticeType = models.ForeignKey('meeting.NoticeType', verbose_name='Tipo de edital', null=True, blank=True)
	link = models.CharField('Link externo para o edital', max_length=500, null=True, blank=True)

	created_at  = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at  = models.DateTimeField('Atualizado em', auto_now=True)

	class Meta:
		verbose_name = "Edital"
		verbose_name_plural = "Editais"

	def __str__(self):
		return self.title
