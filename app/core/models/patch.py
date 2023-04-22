from django.db import models
from core.models import Parameters, ParamValues
from core.models.products import Products




class Patch(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False, help_text="unique name of product")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creation_user_id = models.IntegerField(null=True, blank=True)
    update_user_id = models.IntegerField(null=True, blank=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="product_patch")
    parameters = models.ManyToManyField(Parameters, related_name="patch_paramters")
    value = models.ManyToManyField(ParamValues, related_name="patch_value")
