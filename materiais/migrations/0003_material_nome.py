# Generated by Django 3.2.16 on 2022-10-15 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiais', '0002_tipo_material_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='nome',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
