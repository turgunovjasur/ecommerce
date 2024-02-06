from rest_framework import generics, serializers

from products.models import FlashSale


class FlashSaleListCreateView(generics.ListCreateAPIView):
    queryset = FlashSale.objects.all()

    class FlashSaleSerializer(serializers.ModelSerializer):
        class Meta:
            model = FlashSale
            fields = ('id', 'product', 'discount_percentage', 'start_time', 'end_time')

    serializer_class = FlashSaleSerializer
