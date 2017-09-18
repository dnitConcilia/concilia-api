from django.contrib import admin
from api.news.models import News, CategoryNews
# Register your models here.
admin.site.register([News, CategoryNews])
