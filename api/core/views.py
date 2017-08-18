import json
from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import viewsets

from rest_framework.authtoken.models import Token
from django.contrib.auth import logout
from rest_framework.permissions import AllowAny
from api.news.models import CategoryNews

UserModel = get_user_model()


class ConfigSystemView(viewsets.ModelViewSet):
	permission_classes = (AllowAny,)

	def list(self, request, *args, **kwargs):
		response = {}
		try:
			admin = UserModel.objects.get(username='concilia')
			response['administrador'] = 'Usuário com perfil de administrador já foi criado!'
		except:
			response['administrador'] = 'Usuário com perfil de administrador criado com sucesso!'
			admin = UserModel.objects.create_superuser(
				username='concilia', email='concilia@root.com',
				password='Dnit@123'
			)

		CategoryNews.objects.get_or_create(category='Processo', subCategory='')
		CategoryNews.objects.get_or_create(category='Imóveis', subCategory='')
		CategoryNews.objects.get_or_create(category='Comunidades', subCategory='')
		CategoryNews.objects.get_or_create(category='Conselho Executivo', subCategory='')
		CategoryNews.objects.get_or_create(category='Outros', subCategory='')

		return HttpResponse(
			json.dumps(response),
			content_type="application/json"
		)

class LogoutChangeToken(viewsets.ModelViewSet):

	def list(self, request, *args, **kwargs):
		response = {}
		try:
			key = (self.request.META['HTTP_AUTHORIZATION'].split(" "))[1]
			tk = Token.objects.filter(key=key)
			user = tk[0].user
			tk.delete()
			Token.objects.create(user=user)
			response['message'] = 'Logout realizado com sucesso!'

			return HttpResponse(
				json.dumps(response),
				content_type="application/json"
			)
		except:
			logout(self.request)
			return HttpResponseRedirect("/")
