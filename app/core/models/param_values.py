from django.db import models


class ParamValues(models.Model):
    TYPES = (
        (0, "text"),
        (1, "range"),
    )
    name = models.CharField(max_length=100, unique=True, null=False, blank=False, help_text="unique name of product")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creation_user_id = models.IntegerField(null=True, blank=True)
    update_user_id = models.IntegerField(null=True, blank=True)
    types = models.IntegerField(
        choices=TYPES,
        default=0,
        null=True,
        blank=True,
        help_text="type of range",
    )
    string_value = models.CharField(max_length=100, null=True, blank=True)
    range_value = models.IntegerField(null=True, blank=True)
