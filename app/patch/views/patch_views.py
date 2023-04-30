from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from patch.serializers.patch_serializer import PatchSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import Patch, Parameters
from core.models.param_values import ParamValues


class PatchViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = Patch.objects.all()
        serializer = PatchSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            queryset = Patch.objects.all()
            patch = get_object_or_404(queryset, pk=pk)
            serializer = PatchSerializer(patch)
        
            return Response(serializer.data)
        except Exception as e:
            import traceback
            print(e)
            print(traceback.format_exc())
    
    def create(self, request):
        user = self.request.user
        serializer = PatchSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        patch = Patch.objects.create(**serializer.validated_data, user=user)
        return Response({"message":"created successfully", "id": patch.id}, status=200)
    
    def update(self, request, pk=None):
        user = self.request.user
        if pk is None:
            return Response({"message":"no pk"}, status=400)
        serializer = PatchSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        parameters = serializer.validated_data.get('parameters')
        values = serializer.validated_data.get('value')
        name = serializer.validated_data.get('name')
        product_id = serializer.validated_data.get('product')
        
        try:
            patch = Patch.objects.filter(id=pk).update(name = name, product_id=product_id)
            patch_obj = Patch.objects.filter(id=pk).last()
            for parameter in parameters:
                # par = Parameters.objects.filter(id=parameter).last()
                patch_obj.parameters.add(parameter)
            for value in values:
                # val = ParamValues.objects.filter(id=value).last()
                patch_obj.value.add(value)   
            patch_obj.save()    
        except Exception as e:
            import traceback
            print(e)
            print(traceback.format_exc())
        return Response({"message":"updated successfully"}, status=200)

