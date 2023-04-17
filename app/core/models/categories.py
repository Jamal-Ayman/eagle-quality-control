from django.db import models
from core.models.parameters import Parameters


class Category(models.Models):
    name = models.CharField(max_length=100, unique=True, required=True, help_text="unique name of category")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creation_user_id = models.IntegerField(null=True, max_length=25, blank=True)
    update_user_id = models.IntegerField(null=True, max_length=25, blank=True)
    parameters = models.ManyToManyField(Parameters, related_name="cat_paramters")