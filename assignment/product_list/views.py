from django.shortcuts import render
from .models import Product
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = 'product_list/login.html'
    fields = '__all__'
    redirect_authenticated_user = 'True'

    def get_success_url(self):
        return reverse_lazy('products')


class ProductList(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['products'] = context['products'].filter(user=self.request.user)
    #     context['count'] = context['products'].filter(complete=False).count()
    #     return context


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = 'products'


class ProductCreate(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('products')


class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('products')


class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('products')
