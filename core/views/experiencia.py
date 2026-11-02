from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.models import Experiencia
from core.serializers import ExperienciaSerializer


class ExperienciaViewSet(ReadOnlyModelViewSet):
    queryset = Experiencia.objects.filter(publicado=True)
    serializer_class = ExperienciaSerializer
    permission_classes = (AllowAny,)
