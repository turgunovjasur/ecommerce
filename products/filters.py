from django_filters import rest_framework as django_filters  # pip install django-filter
from .models import Product, Category, FlashSale


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['category', 'min_price', 'max_price']


class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ['name']


class FlashSaleFilter(django_filters.FilterSet):
    class Meta:
        model = FlashSale
        fields = ['start_time', 'end_time']


