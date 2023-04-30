from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from patch.serializers.categories_serializer import CategorySerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import Parameters
from core.models.categories import Category



class CategoryViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    def create(self, request):
        user = self.request.user
        serializer = CategorySerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        category = Category.objects.create(**serializer.validated_data, user=user)
        return Response({"message":"created successfully", "id": category.id}, status=200)
    
    def update(self, request, pk=None):
        user = self.request.user
        if pk is None:
            return Response({"message":"no pk"}, status=400)
        serializer = CategorySerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.get('name')
        parameters = serializer.validated_data.get('parameters')
        
        try:
            category = Category.objects.filter(id=pk).last()
            category.name=name
            for parameter in parameters:
                category.parameters.add(parameter)
            category.save()    
        except Exception as e:
            print(e)    
        return Response({"message":"updated successfully"}, status=200)

