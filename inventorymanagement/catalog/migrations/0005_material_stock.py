# Generated by Django 3.2.9 on 2022-02-08 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_material_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='stock',
            field=models.IntegerField(default=0, help_text='Cantidad existente en pañol.', verbose_name='Stock'),
        ),
    ]
