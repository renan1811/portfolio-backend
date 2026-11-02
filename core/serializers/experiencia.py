from rest_framework.serializers import ModelSerializer

from core.models import Experiencia


class ExperienciaSerializer(ModelSerializer):
    class Meta:
        model = Experiencia
        fields = (
            'id', 'titulo', 'organizacao', 'descricao', 'tipo',
            'data_inicio', 'data_fim', 'atual', 'ordem', 'publicado',
        )
