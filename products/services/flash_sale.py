from django_filters import rest_framework as django_filters
from rest_framework import filters
from datetime import datetime, timedelta
from rest_framework import generics, status
from rest_framework.decorators import api_view

from rest_framework.response import Response

from products.filters import FlashSaleFilter
from products.models import FlashSale, Product, ProductViewHistory
from rest_framework import serializers


class FlashSaleListCreateView(generics.ListCreateAPIView):
    queryset = FlashSale.objects.all()

    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = FlashSaleFilter
    search_fields = ['name', 'description']

    class FlashSaleSerializer(serializers.ModelSerializer):
        class Meta:
            model = FlashSale
            fields = ('id', 'product', 'discount_percentage', 'start_time', 'end_time')

    serializer_class = FlashSaleSerializer


@api_view(['GET'])
def check_flash_sale(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({"error": "Mahsulot topilmadi"}, status=status.HTTP_404_NOT_FOUND)

    user_viewed = ProductViewHistory.objects.filter(user=request.user, product=product).exists()
    upcoming_flash_sale = FlashSale.objects.filter(
        product=product,
        start_time__lte=datetime.now() + timedelta(hours=24)
    ).first()

    if user_viewed and upcoming_flash_sale:
        discount = upcoming_flash_sale.discount_percentage
        start_time = upcoming_flash_sale.start_time
        end_time = upcoming_flash_sale.end_time
        return Response({
            "message": f"Ushbu mahsulot {discount}% chegirmada!",
            "start_time": start_time,
            "end_time": end_time
        })
    else:
        print(request.user.id)
        print(user_viewed)
        print(upcoming_flash_sale)
        return Response({
            "message": "Ushbu mahsulot uchun yaqin orada chegirma yo'q!."
        })
