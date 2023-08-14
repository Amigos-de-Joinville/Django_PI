from rest_framework.viewsets import ModelViewSet

from amigosjvll.models import Cor
from amigosjvll.serializers import CorSerializer


class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer