from django.db import models
from rest_framework import serializers
from .models import Product, Review, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    avg_rating = serializers.FloatField(read_only=True, required=False)
    # read_only=True -> faqat o'qish uchun
    # required=False -> to'ldirish majburiy emas

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'category', 'avg_rating']
