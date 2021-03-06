from audioop import reverse
from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name
    
    
class Cart(models.Model):
    cart_id = models.CharField(max_length=225, unique=True)
    date_added = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("cart:add_to_cart", kwargs={"cart_id": self.cart_id})

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_activate = models.BooleanField(default=True)
    def sub_total(self):
        return self.product.price*self.quantity
    def __str__(self):
        return f'{self.product}'