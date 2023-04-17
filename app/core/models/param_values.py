from django.db import models
from core.models.patch import Patch
from core.models.parameters import Parameters


class ParamValues(models.Model):
    TYPES = (
        (0, "text"),
        (1, "range"),
    )
    name = models.CharField(max_length=100, unique=True, required=True, help_text="unique name of product")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creation_user_id = models.IntegerField(null=True, max_length=25, blank=True)
    update_user_id = models.IntegerField(null=True, max_length=25, blank=True)
    types = models.IntegerField(
        choices=TYPES,
        default=0,
        null=True,
        blank=True,
        help_text="type of range",
    )
    parameters = models.ManyToManyField(Parameters, related_name="value_paramters")
    string_value = models.CharField(max_length=100, null=True, blank=True)
    range_value = models.IntegerField(max_length=100, null=True, blank=True)
