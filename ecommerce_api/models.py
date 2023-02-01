from django.db import models
from django.urls import reverse
from django.conf import settings
User = settings.AUTH_USER_MODEL


class Item(models.Model):
    name=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    photo=models.ImageField(upload_to='images')

    class Meta:
        ordering=['id']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("product_details",kwargs={'id' : self.id})

    def add_to_cart_url(self):
        return reverse("add_to_cart",kwargs={'id' : self.id})

    def remove_from_cart_url(self):
        return reverse(" remove_from_cart",kwargs={'id' : self.id})




class OrderItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
   # ordered=models.BooleanField(default=False)
    quantity=models.IntegerField(default=1)
    
    @property
    def get_total_price(self):
        return self.item.price*self.quantity
    
    def __str__(self):
        return self.user.email[:5]
  
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    items=models.ManyToManyField(OrderItem)
    #ordered=models.BooleanField(default=False)

    def __str__(self):
        return self.user.email[:5] + "'s" + " Order"

    

