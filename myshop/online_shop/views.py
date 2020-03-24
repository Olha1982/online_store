from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, View
from django.contrib.auth.views import LoginView, LogoutView

from online_shop.models import Product


class Registration(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = '/'


class Login(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('index')


class Logout(LoginRequiredMixin, LogoutView):
    def get(self, request, *args, **kwargs):
        logout(request.user)
        return super().get(request, *args, **kwargs)


class ProductListView(ListView):
    model = Product
    template_name = 'product.html'
    queryset = Product.objects.all()
    paginate_by = 3
    ordering = ['name']


