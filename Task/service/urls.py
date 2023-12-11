from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('bag/', bag, name='bag'),
    path('add/<int:product_id>/', add_to_order, name='add_to_order'),
    path('proceed_payment/', proceed_payment, name='payment'),
]
