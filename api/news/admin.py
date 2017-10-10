from django.contrib import admin
from api.news.models import News, CategoryNews, PhotoNews
# Register your models here.
admin.site.register([News, CategoryNews, PhotoNews])
