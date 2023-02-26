# Generated by Django 4.1.6 on 2023-02-26 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Joke",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=True,
                        verbose_name="ID",
                    ),
                ),
                ("joke", models.TextField()),
                ("category", models.CharField(max_length=30)),
            ],
        ),
    ]