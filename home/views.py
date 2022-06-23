from urllib import response
from django.shortcuts import render

from home.models import Cart

# Create your views here.


def _cart_id(request):
    cart = request.session.session_key

    if not cart:
        cart = request.session.create()
    return cart


def home(request):
    cart_session = _cart_id(request)
    print(cart_session)
    return render(request, "index.html", {})


def add_to_cart(request):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        Cart.objects.create(cart_id=_cart_id(request)).save()
    return render(request, "cart.html", {"cart": cart})
