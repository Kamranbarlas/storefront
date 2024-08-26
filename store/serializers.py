from decimal import Decimal
from rest_framework import serializers
from . models import Product, Collection

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id','title','products_count']
    products_count = serializers.IntegerField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory', 'unit_price', 'price_with_tax', 'collection']
    # id  = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=6, decimal_places=2,source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name="calculate_with_tax")
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset = Collection.objects.first(),
    #     view_name = 'collection_detail'
    # )

    def calculate_with_tax(self, product: Product):
        return product.unit_price * Decimal(1.1) 
    
    def create(self, validated_data):
        return super().create(validated_data)