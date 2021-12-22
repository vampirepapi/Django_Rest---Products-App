from rest_framework import serializers
from .models import ProductItem

class ProductItemSerializer(serializers.ModelSerializer):
    # product_id = serializers.IntegerField(required=False, default=1)
    product_name = serializers.CharField(max_length=200)
    product_price = serializers.FloatField()
    product_quantity = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = ProductItem
        fields = ('__all__')