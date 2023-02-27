from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from e_shop.models import Product


def products_list_view(request):
    products_list = Product.objects.all()
    context = {
        'products_list': products_list
    }
    return render(request, 'products_list_page.html', context=context)