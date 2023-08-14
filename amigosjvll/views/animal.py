from rest_framework.viewsets import ModelViewSet

from amigosjvll.models import Animal
from amigosjvll.serializers import AnimalSerializer, AnimalDetailSerializer, AnimalListSerializer


class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return AnimalListSerializer
        elif self.action == "retrieve":
            return AnimalDetailSerializer
        return AnimalSerializer