from django.urls import path

from e_shop.views.product import products_list_view

urlpatterns = [
    path('', products_list_view, name='products_list')
]
