from django import template
from service.models import *
register = template.Library()

@register.filter
def total_price(bag):
    result = 0
    for item in bag:
        result += 1*item.quantity
    return result