from django.shortcuts import get_object_or_404,redirect
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ecommerce_api.models import Item,OrderItem,Order
from .serializer import ItemSerializer,CartSerializer
from rest_framework import status
class ItemsApi(ListAPIView):
    serializer_class = ItemSerializer
    queryset=Item.objects.all()
    
    
class ItemDetailsApi(RetrieveAPIView):
    serializer_class = ItemSerializer
    queryset=Item.objects.all()
    lookup_field='id'

class CartApi(ListAPIView):
    serializer_class=CartSerializer
    queryset=OrderItem.objects.all()

class AddItemToCartView(APIView):
    def post(self, request,id):
        user = request.user
        item = request.data.get('item')
        quantity = request.data.get('quantity', 1)

        cart_item, created = OrderItem.objects.get_or_create(user=user, item=item)
        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        serializer = CartSerializer(cart_item)
        return Response(serializer.data)

    def put(self, request, id):
        cart_item = OrderItem.objects.get(pk=id)
        cart_item.quantity = request.data.get('quantity', cart_item.quantity)
        cart_item.save()

        serializer = CartSerializer(cart_item)
        return Response(serializer.data)


