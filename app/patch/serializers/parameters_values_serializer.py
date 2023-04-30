"""
Serializers for categories api
"""

from rest_framework import serializers
from core.models.param_values import ParamValues


class ParameterValuesSerializer(serializers.ModelSerializer):
    """Serialzer for parameters"""

    class Meta:
        model = ParamValues
        fields = ['name', 'created_at', 
                  'user', 'types', 
                  'string_value', 'range_value']
        read_only_fields = ['created_at', 'user']