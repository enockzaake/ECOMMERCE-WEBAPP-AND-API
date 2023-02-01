from rest_framework import serializers
from ecommerce_api.models import Item,OrderItem



class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields='__all__'  

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields=['item','quantity'] 
        depth=1



    
