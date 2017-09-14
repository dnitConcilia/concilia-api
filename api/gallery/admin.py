from django.contrib import admin
from api.gallery.models import CategoryGallery, Gallery, Photo, Video
# Register your models here.
admin.site.register([CategoryGallery, Gallery, Photo, Video])
