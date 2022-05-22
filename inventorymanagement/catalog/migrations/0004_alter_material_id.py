# Generated by Django 3.2.9 on 2022-02-08 19:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_materialinstance_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='ID único para este material particular en toda la biblioteca', primary_key=True, serialize=False),
        ),
    ]
