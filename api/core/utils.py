from rest_framework.views import exception_handler

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
