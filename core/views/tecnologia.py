from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.models import Tecnologia
from core.serializers import TecnologiaSerializer


class TecnologiaViewSet(ReadOnlyModelViewSet):
    queryset = Tecnologia.objects.all()
    serializer_class = TecnologiaSerializer
    permission_classes = (AllowAny,)
