from django.contrib import admin
from .models import *


class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderItemInline]

admin.site.register(Item)
admin.site.register(Tax)
admin.site.register(Order,OrderAdmin)
admin.site.register(Discount)