# Generated by Django 4.1.6 on 2023-02-26 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("v1", "0003_alter_joke_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="joke",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
