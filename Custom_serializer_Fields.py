from decimal import Decimal
from rest_framework import serializers

from store.models import Product

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length =255)
    #we can also rename our fields, e.g Here we rename unit_price in produsts to price, SInce django assumes unit_price is in products, it will also assume that the renamed field of price is also in the produts, but price is not there, so we have to give the source of this renamed field as 'unit_price' from the product
    price = serializers.DecimalField(max_digits=6,decimal_places=2,source ='unit_price')
    #unit_price = serializers.DecimalField(max_digits=6,decimal_places=2)
    #This is the new custom field  tht is presneted at this end point. It is calculated through the specifie method here below.
    price_with_tax = serializers.SerializerMethodField(method_name= 'calculate_tax')
    
    def calculate_tax(self,product:Product):
        return product.unit_price * Decimal(1.1)






























































































































...
