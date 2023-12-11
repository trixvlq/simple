from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from service.models import *
from .models import Customer
class MyLoginView(LoginView):
    template_name = 'login.html'


def MyLogoutView(request):
    logout(request)
    return redirect('home')


class MyCreateView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        order = Order.objects.create()
        order.save()
        Customer.objects.create(user=self.request.user,bag=order)
