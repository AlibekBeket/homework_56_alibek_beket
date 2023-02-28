from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from e_shop.models import *

from e_shop.forms import ProductForm


def products_list_view(request):
    product_category = ProductCategoryChoice.choices
    products_list = Product.objects.exclude(the_rest_of_the_goods=0).order_by('category', 'product_name')
    for product in products_list:
        for category in product_category:
            if product.category == category[0]:
                product.category = category[1]
    context = {
        'products_list': products_list
    }
    return render(request, 'products_list_page.html', context=context)


def product_detail_view(request, pk):
    product_info = get_object_or_404(Product, pk=pk)
    product_category = ProductCategoryChoice.choices
    for category in product_category:
        if product_info.category == category[0]:
            product_info.category = category[1]
    context = {
        'product': product_info
    }
    return render(request, 'product_detail_page.html', context=context)


def product_add_view(request):
    if not request.POST:
        form = ProductForm()
        context = {
            'form': form
        }
        return render(request, 'product_add_page.html', context=context)
    form = ProductForm(data=request.POST)
    if not form.is_valid():
        context = {
            'form': form
        }
        return render(request, 'product_add_page.html', context=context)
    else:
        product = Product.objects.create(**form.cleaned_data)
        return redirect('product_detail', pk=product.pk)