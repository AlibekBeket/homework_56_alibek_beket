from django.urls import path

from e_shop.views.product import *

urlpatterns = [
    path('', products_list_view, name='products_list'),
    path('product/', products_list_view, name='products_list'),
    path('product/<int:pk>/', product_detail_view, name='product_detail')
]
