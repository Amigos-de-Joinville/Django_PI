# Generated by Django 4.2.4 on 2023-08-27 22:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("amigosjvll", "0010_rename_imagem_animal_foto"),
    ]

    operations = [
        migrations.RenameField(
            model_name="animal",
            old_name="foto",
            new_name="imagem",
        ),
    ]