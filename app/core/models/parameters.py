from django.db import models
from core.models.param_values import ParamValues


class Parameters(models.Model):
    name = models.CharField(max_length=250, unique=True, null=False, blank=False, help_text="unique name of product")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creation_user_id = models.IntegerField(null=True, blank=True)
    update_user_id = models.IntegerField(null=True, blank=True)
    values = models.ForeignKey(ParamValues, on_delete=models.CASCADE, related_name="param_valu")

