# Generated by Django 4.2.4 on 2023-09-06 13:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("amigosjvll", "0012_rename_imagem_animal_foto"),
    ]

    operations = [
        migrations.AddField(
            model_name="animal",
            name="descricao",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
