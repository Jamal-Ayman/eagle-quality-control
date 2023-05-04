from django.contrib import admin
from django.utils.translation import gettext_lazy as _
import re


class InputFilter(admin.SimpleListFilter):
    template = "admin/input_filter.html"

    def lookups(self, request, model_admin):
        return [(1, "")]

    def choices(self, changelist):
        all_choice = next(super().choices(changelist))
        all_choice["query_parts"] = (
            (k, v)
            for k, v in changelist.get_filters_params().items()
            if k != self.parameter_name
        )
        yield all_choice

    def queryset(self, request, queryset):
        if not self.value():
            return queryset


class ProductFilter(InputFilter):
    parameter_name = "product name"
    title = _("Product Name")

    def queryset(self, request, queryset):
        """
        Filter by product name
        """
        # if self.value():
        #     cleaned_query = []
        #     for i in re.split(" |, |,| ,", self.value().rstrip()):
        #         if str.isdigit(i):
        #             cleaned_query.append(i)
        if not self.value():
            return queryset
        
        return queryset.filter(
                product__name__icontains=self.value()
            )

    
class CategoryFilter(InputFilter):
    parameter_name = "category name"
    title = _("Category Name")

    def queryset(self, request, queryset):
        """
        Filter by product name
        """
        if not self.value():
            return queryset
        
        return queryset.filter(
                category__name__icontains=self.value()
            )    