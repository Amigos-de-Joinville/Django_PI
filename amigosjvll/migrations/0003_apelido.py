# Generated by Django 4.2.4 on 2023-08-13 23:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("amigosjvll", "0002_raca"),
    ]

    operations = [
        migrations.CreateModel(
            name="Apelido",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
            ],
        ),
    ]