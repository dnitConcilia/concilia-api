from rest_framework.views import exception_handler
from django.template.defaultfilters import slugify
import time

def custom_exception_handler(exc, context):
	response = exception_handler(exc, context)

	try:
		if 'non_field_errors' in response.data:
			response.data['message'] = response.data['non_field_errors']
			response.data['type'] = 'non_field_errors'
	except:
		pass

	return response

def formatDate(date, separator):
	date = date.split(separator)
	return date[2] + "-" + date[1] + "-" + date[0]

def slugifyTitle(title, date=None):
	slug = ''
	try:
		slug = slugify(title)
	except Exception as e:
		if date:
			slug = slugify(title + date)
		else:
			slug = slugify(title + time.strftime("%d-%m-%Y"))
	return slug
