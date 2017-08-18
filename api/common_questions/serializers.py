from rest_framework import serializers
from api.common_questions.models import CategoryFaq, Faq


class CategoryFaqReadSerializer(serializers.ModelSerializer):

	class Meta:
		model   = CategoryFaq
		exclude = ('created_at', 'updated_at')


class CategoryFaqWriteSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		catFaq, created = CategoryFaq.objects.get_or_create(**validated_data)
		return catFaq

	class Meta:
		model   = CategoryFaq
		exclude = ('id', 'created_at', 'updated_at')

class FaqReadSerializer(serializers.ModelSerializer):
	category = CategoryFaqReadSerializer(many=False)

	class Meta:
		model = Faq
		exclude = ('created_at', 'updated_at')


class FaqWriteSerializer(serializers.ModelSerializer):
	id_categoryFaq = serializers.IntegerField(write_only=True, required=False)

	def create(self, validated_data):
		errors = {
			'fields_error': {},
			'hasError': False
		}
		if 'id_categoryFaq' not in validated_data:
			errors['fields_error']['id_categoryFaq'] = {
				'message': 'O campo de categoria da pergunta é obrigatório',
				'type': 'FieldRequired'
			}
			errors['hasError'] = True

		catFaq = None
		try:
			catFaq = CategoryFaq.objects.get(pk=validated_data.pop('id_categoryFaq'))
		except Exception as ObjectDoesNotExist:
			errors['fields_error']['id_categoryFaq'] = {
				'message': 'Não foi encontrada categoria com esse ID',
				'type': 'ObjectDoesNotExist'
			}
			errors['hasError'] = True

		faq, created = Faq.objects.get_or_create(
			question=validated_data.pop('question'),
			answer=validated_data.pop('answer'),
			category=category
		)

		return faq

	def update(self, instance, validated_data):
		errors = {
			'fields_error': {},
			'hasError': False
		}
		if 'id_categoryFaq' not in validated_data:
			errors['fields_error']['id_categoryFaq'] = {
				'message': 'O campo de categoria da pergunta é obrigatório',
				'type': 'FieldRequired'
			}
			errors['hasError'] = True

		try:
			catFaq = CategoryFaq.objects.get(pk=validated_data.pop('id_categoryFaq'))
		except Exception as ObjectDoesNotExist:
			errors['fields_error']['id_categoryFaq'] = {
				'message': 'Não foi encontrada categoria com esse ID',
				'type': 'ObjectDoesNotExist'
			}
			errors['hasError'] = True

		Faq.objects.filter(pk=instance.pk).update(
			question=validated_data.pop('question'),
			answer=validated_data.pop('answer'),
			category=category
		)

		return instance

	class Meta:
		model = Faq
		exclude = ('id', 'category', 'created_at', 'updated_at')
