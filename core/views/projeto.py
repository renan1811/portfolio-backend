from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.models import Projeto
from core.serializers import ProjetoSerializer


class ProjetoViewSet(ReadOnlyModelViewSet):
    queryset = Projeto.objects.filter(publicado=True).prefetch_related('tecnologias')
    serializer_class = ProjetoSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'slug'
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('destaque',)
