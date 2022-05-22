from django.db import models
from django.urls import reverse
from django.conf import settings
from .lang_spa import *
import uuid


class System(models.Model):
    name = models.CharField(max_length=200, help_text=SYSTEM_NAME_HELP)

    def __str__(self):
        return self.name


class Trademark(models.Model):
    name = models.CharField(TRADEMARK_NAME, max_length=200, help_text=TRADEMARK_NAME_HELP)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('trademark-detail', args=[str(self.id)])


class Material(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text=MATERIAL_NAME_HELP)
    description = models.TextField(MATERIAL_DESCRIPTION, max_length=500)
    position = models.CharField(MATERIAL_POSITION, max_length=50, null=True)
    owner = models.CharField(MATERIAL_OWNER, max_length=20, null=True, help_text=MATERIAL_OWNER_HELP)
    value = models.IntegerField(MATERIAL_VALUE, default=0, null=True, blank=True, help_text=MATERIAL_VALUE_HELP)
    stock = models.IntegerField(MATERIAL_STOCK_NAME, blank=False, null=False, default=0, help_text=MATERIAL_STOCK_HELP)
    safety_stock = models.IntegerField(MATERIAL_SAFETY_NAME, blank=True, null=True, help_text=MATERIAL_SAFETY_HELP)
    last_entry = models.DateTimeField(null=True, blank=True)
    trademark = models.ForeignKey(Trademark, on_delete=models.SET_NULL, null=True)
    system = models.ForeignKey(System, on_delete=models.SET_NULL, null=True, help_text=MATERIAL_SYSTEM_HELP)
    STATUS = (('d', MATERIAL_STATUS_AVAILABLE), ('r', MATERIAL_STATUS_RESERVED))
    status = models.CharField(max_length=1, choices=STATUS, blank=True, default='d', help_text=MATERIAL_STATUS_HELP)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('material-detail', args=[str(self.id)])


class MaterialHistory(models.Model):
    OPERATION = (('e', 'Entrada'), ('s', 'Salida'))
    operation = models.CharField(max_length=1, choices=OPERATION)
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.material.description


