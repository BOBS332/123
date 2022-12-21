from simpleapp.filters import ProductFilter

from .models import Product

from .forms import ProductForm
from .forms import ProductForm, UserRegistrationForm
from .forms import ProductForm, UserRegistrationForm
from django.views.generic import (

    ListView, DetailView, CreateView, FormView
)
from django.contrib.auth import get_user_model
from django.urls import reverse


from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'


User = get_user_model()


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 2
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ProductDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Product
    # Используем другой шаблон — product.html
    template_name = 'product.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'product'
    pk_url_kwarg = 'id'


class ProductCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = ProductForm
    # модель товаров
    model = Product
    # и новый шаблон, в котором используется форма.
    template_name = 'product_edit.html'


class RegisterUserView(FormView):
    form_class = UserRegistrationForm
    template_name = 'registration.html'

    def get_success_url(self) -> str:
        return reverse('products:product-list')

    def post(self, request, *args: str, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = User(username=form.data['username'])
            user.set_password(form.data['password'])
            user.save()

        return super().post(request, *args, **kwargs)
