from rest_framework.serializers import ModelSerializer

from amigosjvll.models import Raca


class RacaSerializer(ModelSerializer):
    class Meta:
        model = Raca
        fields = "__all__"