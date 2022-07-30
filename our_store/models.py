from email.policy import default
from django.db import models
from django.conf import settings

class Item(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    def __str__(self):
        return self.title

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
            return self.title

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()    
    ordered = models.BooleanField(default=False)

    def __str__(self):
            return self.user.username