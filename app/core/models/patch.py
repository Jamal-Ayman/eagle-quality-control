from django.db import models
from core.models.products import Products
from core.models.parameters import Parameters
from core.models.param_values import ParamValues


class Patch(models.Model):
    name = models.CharField(max_length=100, unique=True, required=True, help_text="unique name of product")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creation_user_id = models.IntegerField(null=True, max_length=25, blank=True)
    update_user_id = models.IntegerField(null=True, max_length=25, blank=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="product_patch")
    parameters = models.ManyToManyField(Parameters, related_name="patch_paramters")
    value = models.ManyToManyField(ParamValues, related_name="patch_value")
