# Generated by Django 5.1 on 2024-11-28 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0002_remove_noticia_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
