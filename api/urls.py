from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



from .views import ItemsApi,ItemDetailsApi,CartApi,AddItemToCartView

urlpatterns = [
    path('all-items/',ItemsApi.as_view(),name='all-items'),
    path('item/<id>/',ItemDetailsApi.as_view(),name='item'),
    path('cart-api/',CartApi.as_view(),name='cart-api'),
    path('add-to-cart-api/',AddItemToCartView.as_view(),name='add-to-cart-api'),

]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


