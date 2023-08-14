from rest_framework.viewsets import ModelViewSet

from amigosjvll.models import Raca
from amigosjvll.serializers import RacaSerializer


class RacaViewSet(ModelViewSet):
    queryset = Raca.objects.all()
    serializer_class = RacaSerializer
