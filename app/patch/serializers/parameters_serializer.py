"""
Serializers for categories api
"""

from rest_framework import serializers
from core.models import Parameters
from patch.serializers.parameters_values_serializer import ParameterValuesSerializer

class ParameterSerializer(serializers.ModelSerializer):
    """Serialzer for parameters"""
    # value_details = ParameterValuesSerializer()
    class Meta:
        model = Parameters
        fields = ['name', 'created_at', 'user', 'values', 'value_details']
        read_only_fields = ['created_at', 'user']