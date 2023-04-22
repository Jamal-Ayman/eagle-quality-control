from django.db import models
from core.models import Parameters

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False, help_text="unique name of category")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creation_user_id = models.IntegerField(null=True, blank=True)
    update_user_id = models.IntegerField(null=True,  blank=True)
    parameters = models.ManyToManyField(Parameters, related_name="cat_paramters")