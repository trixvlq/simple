from django.core.validators import MinValueValidator
from django.db import models


class Discount(models.Model):
    text = models.CharField(max_length=100)
    percent = models.PositiveIntegerField()


class Order(models.Model):
    items = models.ManyToManyField("Item", default=None, blank=True, through="OrderItem")


class OrderItem(models.Model):
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f'{self.item.name} to {self.order.customer_bag}'

    def get_price(self):
        return self.item.price * self.quantity


class Tax(models.Model):
    TAX_CHOICES = (
        ("txcd_99999999", "General - Tangible Goods"),
        ("txcd_20030000", "General - Services"),
        ("txcd_10000000", "General - Electronically Supplied Services"),
        ("txcd_00000000", "Nontaxable"),
    )
    name = models.CharField(choices=TAX_CHOICES, default=("txcd_00000000", "Nontaxable"), max_length=100)

    def get_code(self):
        for code, tax_name in self.TAX_CHOICES:
            if tax_name == self.name:
                return code
        return None

    def __str__(self):
        return self.name


class Item(models.Model):
    CURRENCY_CHOICES = (
        ('$', 'USD'),
        ('€', 'EUR'),
        ('₺', 'TRY'),
        ('¥', 'JPY')
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    currency = models.CharField(max_length=20, choices=CURRENCY_CHOICES, default=('$', 'dollar'))
    image = models.ImageField(upload_to='static/images/%Y/%m/%d/', blank=True)
    amount = models.IntegerField(default=0)
    tax = models.ForeignKey("Tax", on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name

    def get_currency_sign(self):
        return self.currency

    def get_currency(self):
        return dict(Item.CURRENCY_CHOICES).get(self.currency, '')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
