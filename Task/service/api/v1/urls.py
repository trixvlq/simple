from django.urls import path

from .views import *
urlpatterns = [
    path('buy/<int:id>/<str:cur>/', buy,name='buy'),
    path('buy/<int:id>/', buy,name='buy'),
    path('get/<int:id>/', get_product,name='get'),
]
