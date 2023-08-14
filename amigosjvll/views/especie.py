from rest_framework.viewsets import ModelViewSet

from amigosjvll.models import Especie
from amigosjvll.serializers import EspecieSerializer

# from rest_framework.permissions import IsAuthenticated


class EspecieViewSet(ModelViewSet):
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer
    # permission_classes = [IsAuthenticated]