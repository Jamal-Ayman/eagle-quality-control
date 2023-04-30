from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from patch.serializers.products_serializer import ProductsSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models.products import Products


class ProductViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = Products.objects.all()
        serializer = ProductsSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Products.objects.all()
        parameter = get_object_or_404(queryset, pk=pk)
        serializer = ProductsSerializer(parameter)
        try:
            return Response(serializer.data)
        except Exception as e:
            print(e)
    
    def create(self, request):
        user = self.request.user
        serializer = ProductsSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        parameter = Products.objects.create(**serializer.validated_data, user=user)
        return Response({"message":"created successfully", "id": parameter.id}, status=200)
    
    def update(self, request, pk=None):
        user = self.request.user
        if pk is None:
            return Response({"message":"no pk"}, status=400)
        serializer = ProductsSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.get('name')
        
        try:
            parameter = Products.objects.filter(id=pk).update(**serializer.validated_data)
        except Exception as e:
            print(e)    
        return Response({"message":"updated successfully"}, status=200)

