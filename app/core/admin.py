"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from core.models import Patch
from core.models import Parameters
from core.models.products import Products
from core.models.param_values import ParamValues
from core.models.categories import Category
from core.admin_utils import ProductFilter, CategoryFilter
from rangefilter.filter import DateTimeRangeFilter

# Register your models here.
from core.models.user_table import User

class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )

class PatchAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'user', 'product']
    list_filter = [("created_at", DateTimeRangeFilter), ProductFilter]
    readonly_fields = ['created_at']
    search_fields = [
        "name",
        "product",
    ]

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'user', 'category']
    list_filter = [("created_at", DateTimeRangeFilter), CategoryFilter]
    readonly_fields = ['created_at']
    search_fields = [
        "name",
    ]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'user']
    list_filter = [("created_at", DateTimeRangeFilter)]
    readonly_fields = ['created_at']
    search_fields = [
        "name",
    ]


admin.site.register(User, UserAdmin)
admin.site.register(Patch, PatchAdmin)
admin.site.register(ParamValues)
admin.site.register(Parameters)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Products, ProductAdmin)