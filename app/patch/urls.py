"""
URL mappings for the recipe app.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from patch import views

router = DefaultRouter()
router.register('category', views.CategoryViewSet, 'category')
router.register('parameter', views.ParameterViewSet, 'parameter')
router.register('product', views.ProductViewSet, 'product')
router.register('patch', views.PatchViewSet, 'patch')
router.register('paramvalue', views.ParamValuesViewSet, 'paramvalue')


app_name = 'patch'

urlpatterns = [
    path('', include(router.urls)),
]