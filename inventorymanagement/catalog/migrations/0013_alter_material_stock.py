# Generated by Django 3.2.9 on 2022-02-16 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_materialhistory_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='stock',
            field=models.IntegerField(default=0, help_text='Cantidad existente en pañol', verbose_name='Stock'),
        ),
    ]
