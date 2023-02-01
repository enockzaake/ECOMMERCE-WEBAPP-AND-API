from django.shortcuts import render,redirect,get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from.models import Item
from django.views.generic import ListView,DetailView
from .models import Item,OrderItem,Order


# display all items 
#@login_required(login_url='login')
class ItemsView(ListView):
    paginate_by=5
    model=Item
    template_name='items.html'

def product_details(request,id):
    item=Item.objects.get(pk=id)
    return render(request,'product_detail.html',{'item':item})
    
@login_required(login_url='login')
def cart(request):
    order = OrderItem.objects.all()     
    cart_total=0
    for item in order:
        cart_total+=item.get_total_price
    return render(request,'cart.html',{'orders':order,'cart_total':cart_total})
    
    
def add_to_cart(request,id):
    item=get_object_or_404(Item,id=id)
    order_item,created = OrderItem.objects.get_or_create(user=request.user,item=item)
    order_qs = Order.objects.filter(user=request.user).order_by('id')
    if order_qs.exists():
        order=order_qs[0]
        if order.items.filter(item__id = item.id).exists():
            order_item.quantity+=1
            order_item.save()
            return redirect('items')
        else:
            order.items.add(order_item)
            return redirect('items')
    else:
        order=Order.objects.create(user=request.user)
        order.items.add(order_item)
        order.save()
    return redirect('items')
                                                                                                                                                                               
def remove_from_cart(request,id):
    item=get_object_or_404(Item,id=id)
    order_item = OrderItem.objects.get(user=request.user,item=item)
    if order_item:
        order_item.delete()
    else:
        pass
    return redirect('cart')

def reduce_quantity(request,id):
    item=get_object_or_404(Item,id=id)
    order_item = OrderItem.objects.get(user=request.user,item=item)
    if order_item.quantity > 1:
        order_item.quantity-=1
        order_item.save()
    else:
        order_item.delete()
    return redirect('cart')

def increase_quantity(request,id):
    item=get_object_or_404(Item,id=id)
    order_item = OrderItem.objects.get(user=request.user,item=item)
    order_item.quantity+=1
    order_item.save()
    return redirect('cart')







