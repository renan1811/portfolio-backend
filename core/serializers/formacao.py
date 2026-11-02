from rest_framework.serializers import ModelSerializer

from core.models import Formacao


class FormacaoSerializer(ModelSerializer):
    class Meta:
        model = Formacao
        fields = (
            'id', 'instituicao', 'curso', 'descricao', 'data_inicio',
            'data_fim', 'em_andamento', 'ordem', 'publicado',
        )
