from django.urls import path
from .views import ProductsList, ProductDetail, ProductCreate


urlpatterns = [
   path('', ProductsList.as_view(), name="product-list"),
   path('<int:id>', ProductDetail.as_view(), name="product-detail"),
   path('create/', ProductCreate.as_view(), name='product_create'),
]
