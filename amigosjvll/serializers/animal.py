from rest_framework.serializers import ModelSerializer, SlugRelatedField, CharField

from uploader.models import Image
from uploader.serializers import ImageSerializer

from amigosjvll.models import Animal


class AnimalSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    foto = ImageSerializer(required=False, read_only=True)
    
    class Meta:
        model = Animal
        fields = "__all__"


class AnimalDetailSerializer(ModelSerializer):
    
    foto = CharField(source="foto.url")
    
    class Meta:
        model = Animal
        fields = "__all__"
        depth = 1


class AnimalListSerializer(ModelSerializer):
    foto = CharField(source="foto.url")
    raca = CharField(source='raca.nome')  # OK
    especie = CharField(source='especie.descricao') # Mudar para especie
    
    class Meta:
        model = Animal
        fields = ["id", "raca", "especie", "foto", "nome", "descricao"] # colocar os nomes da model

