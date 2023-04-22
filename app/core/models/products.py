from django.db import models
from core.models.categories import Category

class Products(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False, help_text="unique name of product")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creation_user_id = models.IntegerField(null=True,  blank=True)
    update_user_id = models.IntegerField(null=True,  blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, related_name="category_product")
