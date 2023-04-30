"""
Serializers for categories api
"""

from rest_framework import serializers

from core.models.categories import Category
from patch.serializers.parameters_serializer import ParameterSerializer 


class CategorySerializer(serializers.ModelSerializer):
    """Serialzer for categories"""
    # parameters = ParameterSerializer(many=True, required=False)

    class Meta:
        model = Category
        fields = ['name', 'created_at', 'user', 'parameters']
        read_only_fields = ['created_at', 'user']
