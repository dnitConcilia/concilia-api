from django.contrib import admin
from api.common_questions.models import CategoryFaq, Faq
# Register your models here.
admin.site.register([CategoryFaq, Faq])
