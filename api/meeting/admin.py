from django.contrib import admin
from api.meeting.models import Meeting, Notice, NoticeType
# Register your models here.
admin.site.register([Meeting, Notice, NoticeType])
