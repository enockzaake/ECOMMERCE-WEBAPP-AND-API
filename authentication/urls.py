from django.urls import path

from .views import Register,user_login



#urls for authentication
urlpatterns = [
    path('register/',Register,name='register'),
    path('login/',user_login,name='login'),
    path('logout/',user_login,name='logout'),
]








