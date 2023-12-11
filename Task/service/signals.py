from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import stripe

from users.models import Customer
from .models import Item, Discount, Order
from decouple import config
stripe.api_key = config("api_key")

@receiver(post_save, sender=Discount)
def create_coupon(sender, instance, **kwargs):
    coupons = stripe.Product.list()
    coupon = [i for i in coupons.auto_paging_iter() if i.name == instance.text]
    if len(coupon) == 0:
        stripe.Coupon.create(
            duration="once",
            name=instance.text,
            percent_off=instance.percent
        )

@receiver(post_save, sender=Item)
def create_product(sender, instance, **kwargs):
    products = stripe.Product.list()
    product = [i for i in products.auto_paging_iter() if i.name == instance.name]
    print(instance.tax.get_code())
    if len(product) == 0:
        item = stripe.Product.create(
            name=instance.name,
            description=instance.description,
            active=True,
            tax_code=instance.tax.get_code() if instance.tax.get_code() else "txcd_00000000",
            default_price_data={
                'currency': instance.get_currency(),
                'unit_amount': instance.price * 100
            },
        )


@receiver(post_delete, sender=Item)
def delete_product(sender, instance, **kwargs):
    products = stripe.Product.list()
    product = [i for i in products.auto_paging_iter() if i.name == instance.name]
    if len(product) == 1:
        stripe.Product.modify(product[0]['id',"active":False])

@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        order = Order.objects.create()
        Customer.objects.get_or_create(
            user=instance,
            defaults={'bag': order}
        )