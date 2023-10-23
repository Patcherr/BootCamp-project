from django.db import models
from clients.models import ClientModel

# Create your models here.

class cart(models.Model):
    user = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} cart "
    
class CarItem(models.Model):
    cart = models.ForeignKey('cart', on_delete=models.CASCADE)
    product = models.ForeignKey(stock_product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.quantity * self.product.price
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name_product} en {self.cart}" 