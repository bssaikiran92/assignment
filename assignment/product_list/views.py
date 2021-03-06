from django.shortcuts import render
from .models import Product
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from django.shortcuts import redirect


class CustomLoginView(LoginView):
    template_name = 'product_list/login.html'
    fields = '__all__'
    redirect_authenticated_user = 'True'

    def get_success_url(self):
        return reverse_lazy('products')


class RegisterPage(FormView):
    template_name = 'product_list/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('products')
        return super(RegisterPage, self).get(*args, **kwargs)


class ProductList(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = context['products'].filter(product=self.request.user)
        context['count'] = context['products'].count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['products'] = context['products'].filter(
                title__contains=search_input
            )
        context['search_input'] = 'search_input'

        return context


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = 'products'


class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['title', 'description']
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        form.instance.product = self.request.user
        return super(ProductCreate, self).form_valid(form)


class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['title', 'description']
    success_url = reverse_lazy('products')


class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('products')



