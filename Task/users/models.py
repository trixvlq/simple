from django.contrib.auth.models import User
from django.db import models
from service.models import Order

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    bag = models.OneToOneField(Order, on_delete=models.PROTECT, related_name="customer_bag")

    def __str__(self):
        return self.user.username
