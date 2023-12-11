from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.models import Customer
from .models import *
from .services import create_items_session


def index(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'index.html', context)


@login_required()
def bag(request):
    customer = Customer.objects.select_related("bag").get(user=request.user)

    context = {
        "bag": customer.bag.items.through.objects.filter(order=customer.bag)
    }

    return render(request, 'bag.html', context)


@login_required()
def proceed_payment(request):
    selected_currency = request.GET.get('currency', 'USD')
    coupon = request.GET.get('coupon')
    customer = Customer.objects.select_related("bag").get(user=request.user)
    bag = customer.bag.items.through.objects.filter(order=customer.bag)
    success_url = create_items_session(bag, selected_currency, coupon).url
    customer.bag.items.clear()
    return redirect(success_url)


@login_required()
def add_to_order(request, product_id):
    customer = Customer.objects.get(user=request.user)
    item, created = OrderItem.objects.get_or_create(order=customer.bag, item=Item.objects.get(id=product_id),
                                                    quantity=1)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('home')
