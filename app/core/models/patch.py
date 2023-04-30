from django.db import models
from core.models import Parameters
from core.models.products import Products
from core.models.param_values import ParamValues
from patch.serializers.parameters_serializer import ParameterSerializer 
from patch.serializers.parameters_values_serializer import ParameterValuesSerializer 
from patch.serializers.products_serializer import ProductsSerializer 




class Patch(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False, help_text="unique name of product")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True)
    update_user_id = models.IntegerField(null=True, blank=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="product_patch")
    parameters = models.ManyToManyField(Parameters, related_name="patch_paramters", null=True, blank=True)
    value = models.ManyToManyField(ParamValues, related_name="patch_value", null=True, blank=True)

    @property
    def values_details(self):
        values = self.value.all()
        value_list = []
        for p in values:
            serializer = ParameterValuesSerializer(p)
            value_list.append(serializer.data)
        return value_list
    
    @property
    def product_details(self):
        product = self.product
        serializer = ProductsSerializer(product)
        return serializer.data
    
    @property
    def parameters_details(self):
        parameter = self.parameters.all()
        param_list = []
        for p in parameter:
            serializer = ParameterSerializer(p)
            print(serializer)
            param_list.append(serializer.data)
        return param_list