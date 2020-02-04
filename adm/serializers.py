from rest_framework import serializers

from .models import *

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product-detail'
    )
    
    class Meta:
        model = Product
        fields = ['name', 'unit_price', 'products']

class StoreSerializer(serializers.HyperlinkedModelSerializer):
    stores = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='store-detail'
    )

    class Meta:
        model = Store
        fields = ['store_name', 'store_location', 'agent', 'stores']

class StockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock
        fields = ['product', 'stock_count', 'store', 'stock_type']