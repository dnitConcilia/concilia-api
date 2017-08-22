from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.documents.models import Documents
from api.documents.serializers import DocumentsReadSerializer, DocumentsWriteSerializer


class DocumentsViewSet(viewsets.ModelViewSet):
	serializer_class = DocumentsReadSerializer
	queryset = Documents.objects.all()
	permission_classes = (IsAuthenticated,)

	def get_serializer_class(self):
		serializer_class = self.serializer_class

		if self.request.method == 'PUT' or \
			self.request.method == 'PATCH' or \
			self.request.method == 'POST':
			serializer_class = DocumentsWriteSerializer

		return serializer_class
