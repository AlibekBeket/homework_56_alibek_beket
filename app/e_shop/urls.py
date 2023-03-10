from django.urls import path

from e_shop.views.product import *

urlpatterns = [
    path('', products_list_view, name='products_list'),
    path('product/', products_list_view, name='products_list'),
    path('product/<int:pk>/', product_detail_view, name='product_detail'),
    path('product/add/', product_add_view, name='product_add'),
    path('product/<int:pk>/update', product_update_view, name='product_update'),
    path('product/<int:pk>/delete', product_delete_view, name='product_delete'),
    path('product/<int:pk>/confirm_delete', product_confirm_delete_view, name='product_confirm_delete')
]
