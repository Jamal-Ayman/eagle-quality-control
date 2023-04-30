"""
Serializers for categories api
"""

from rest_framework import serializers
from core.models import Patch



class PatchSerializer(serializers.ModelSerializer):
    """Serialzer for parameters"""
    class Meta:
        model = Patch
        fields = ['name', 'created_at', 
                'user', 'product', 'parameters',
                'value', 'parameters_details','values_details', 'product_details']
        read_only_fields = ['created_at', 'user']