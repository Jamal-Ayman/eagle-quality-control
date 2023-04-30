"""
Serializers for categories api
"""

from rest_framework import serializers
from core.models.products import Products


class ProductsSerializer(serializers.ModelSerializer):
    """Serialzer for parameters"""

    class Meta:
        model = Products
        fields = ['name', 'created_at', 'user', 'category', "category_details"]
        read_only_fields = ['created_at', 'user']