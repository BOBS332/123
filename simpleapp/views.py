from datetime import  datetime

from .models import Product
from .forms import ProductForm
from .filters import ProductFilter
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView
)

class ProductsList(ListView):
    model = Product

    ordering = 'name'

    template_name = 'products.html'

    context_object_name = 'products'

    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['time_now'] = datetime.utcnow()

        context['next_sale'] = 'Распродажа в среду!'
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