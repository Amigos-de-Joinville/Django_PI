from rest_framework.serializers import ModelSerializer

from rest_framework.serializers import ModelSerializer, SlugRelatedField

# from uploader.models import Image
# from uploader.serializers import ImageSerializer

from amigosjvll.models import Animal


class AnimalSerializer(ModelSerializer):
    # capa_attachment_key = SlugRelatedField(
    #     source="capa",
    #     queryset=Image.objects.all(),
    #     slug_field="attachment_key",
    #     required=False,
    #     write_only=True,
    # )
    # capa = ImageSerializer(required=False, read_only=True)
    
    class Meta:
        model = Animal
        fields = "__all__"


class AnimalDetailSerializer(ModelSerializer):
    # capa = ImageSerializer(required=False)
    
    class Meta:
        model = Animal
        fields = "__all__"
        depth = 1


class AnimalListSerializer(ModelSerializer):
    class Meta:
        model = Animal
        fields = ["id", "marca", "modelo"]

