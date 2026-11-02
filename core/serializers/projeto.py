from rest_framework import serializers

from core.models import Projeto

from .tecnologia import TecnologiaSerializer


class ProjetoSerializer(serializers.ModelSerializer):
    tecnologias = TecnologiaSerializer(many=True, read_only=True)
    imagem = serializers.ImageField(read_only=True)

    class Meta:
        model = Projeto
        fields = (
            'id', 'titulo', 'slug', 'resumo', 'descricao', 'imagem',
            'url_github', 'url_demo', 'tecnologias', 'ano', 'destaque',
            'publicado', 'ordem', 'criado_em', 'atualizado_em',
        )
