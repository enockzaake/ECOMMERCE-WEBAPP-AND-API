from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .views import ItemsView,product_details,add_to_cart,cart,remove_from_cart,increase_quantity,reduce_quantity



urlpatterns=[
    path('',ItemsView.as_view(),name='items'),
    path('product_details/<id>/',product_details,name='product_details'),
    path('add_to_cart/<id>/',add_to_cart,name='add_to_cart'),
    path('cart/',cart,name='cart'),
    path('remove_from_cart/<id>/',remove_from_cart,name='remove_from_cart'),
    path('increase_quantity/<id>/',increase_quantity,name='increase_quantity'),
    path('reduce_quantity/<id>/',reduce_quantity,name='reduce_quantity'),
    
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

