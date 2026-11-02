from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.models import Formacao
from core.serializers import FormacaoSerializer


class FormacaoViewSet(ReadOnlyModelViewSet):
    queryset = Formacao.objects.filter(publicado=True)
    serializer_class = FormacaoSerializer
    permission_classes = (AllowAny,)
