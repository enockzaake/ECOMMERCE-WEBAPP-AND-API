from django.shortcuts import get_object_or_404,redirect
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ecommerce_api.models import Item,OrderItem,Order
from .serializer import ItemSerializer,CartSerializer

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
    def post(self, request):
        item = Item.objects.get(id=request.data.get('item_id'))
        cart = OrderItem.objects.get(id=request.data.get('cart_id'))
        cart.items.add(item)
        cart.save()
        serializer = CartSerializer(cart)
        return Response(serializer.data)























# @api_view(['POST'])
# def addtocartapi(request,id):
#     item=get_object_or_404(Item,id=id)
#     order_item,created = OrderItem.objects.get_or_create(user=request.user,item=item)
#     order_qs = Order.objects.filter(user=request.user).order_by('id')
#     if order_qs.exists():
#         order=order_qs[0]
#         if order.items.filter(item__id = item.id).exists():
#             order_item.quantity+=1
#             order_item.save()
#             return redirect('api/cart-api')
#         else:
#             order.items.add(order_item)
#             return redirect('api/cart-api')
#     else:
#         order=Order.objects.create(user=request.user)
#         order.items.add(order_item)
#         order.save()
#     return redirect('api/cart-api')
  