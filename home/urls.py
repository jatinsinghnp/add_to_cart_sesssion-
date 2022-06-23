from django.urls import path
from .views import home,add_to_cart
urlpatterns = [
    path('',home,name="home"),
    path('add/',add_to_cart,name='add')
]
