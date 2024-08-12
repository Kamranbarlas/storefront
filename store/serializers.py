from decimal import Decimal
from rest_framework import serializers
from . models import Product, Collection

class CollectionSerializer(serializers.Serializer):
    id  = serializers.IntegerField()
    title = serializers.CharField(max_length=255)


class ProductSerializer(serializers.Serializer):
    id  = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2,source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name="calculate_with_tax")
    collection = serializers.HyperlinkedRelatedField(
        queryset = Collection.objects.first(),
        view_name = 'collection_detail'
    )

    def calculate_with_tax(self, product: Product):
        return product.unit_price * Decimal(1.1) 