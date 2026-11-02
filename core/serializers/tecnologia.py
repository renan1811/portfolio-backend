from rest_framework.serializers import ModelSerializer

from core.models import Tecnologia


class TecnologiaSerializer(ModelSerializer):
    class Meta:
        model = Tecnologia
        fields = ('id', 'nome', 'slug', 'icone', 'categoria', 'ordem')
