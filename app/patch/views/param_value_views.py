from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from patch.serializers.parameters_values_serializer import ParameterValuesSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from core.models.param_values import ParamValues


class ParamValuesViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = ParamValues.objects.all()
        serializer = ParameterValuesSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
     
        queryset = ParamValues.objects.all()
        patch = get_object_or_404(queryset, pk=pk)
        serializer = ParameterValuesSerializer(patch)
    
        return Response(serializer.data)
        
    
    def create(self, request):
        user = self.request.user
        serializer = ParameterValuesSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        patch = ParamValues.objects.create(**serializer.validated_data, user=user)
        return Response({"message":"created successfully", "id": patch.id}, status=200)
    
    def update(self, request, pk=None):
        user = self.request.user
        if pk is None:
            return Response({"message":"no pk"}, status=400)
        serializer = ParameterValuesSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            patch = ParamValues.objects.filter(id=pk).update(**serializer.validated_data)
        except Exception as e:
            import traceback
            print(e)
            print(traceback.format_exc())
        return Response({"message":"updated successfully"}, status=200)

