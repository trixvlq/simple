from django.http import JsonResponse
from django.shortcuts import render

from service.models import Item
from service.services import *


def buy(request, id, cur="USD"):
    item = Item.objects.get(id=id)
    result = create_item_session(item,prefered_payment=cur)
    return JsonResponse({"session_id": result.id})


def get_product(request, id):
    item = Item.objects.get(id=id)
    result = create_item_session(item)
    context = {
        'item':item
    }
    return render(request,'product.html',context)
