from typing import Optional
from django.db import models
from django.db.models.fields import AutoField, FloatField, IntegerField, TextField
from django.db.models.fields.files import ImageField

# Create your models here.
class Products(models.Model):
    uid = AutoField(primary_key=True, editable=False)
    name = TextField(max_length=30, null=False)
    price = FloatField(null=False, default=0,)
    description = TextField(max_length=500, null=False)

    def __str__(self):
        return self

