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

def product_update_view(request, pk):
    product_info = get_object_or_404(Product, pk=pk)
    product_info_dict = {
        'product_name': product_info.product_name,
        'product_description': product_info.product_description,
        'product_image': product_info.product_image,
        'category': product_info.category,
        'the_rest_of_the_goods': product_info.the_rest_of_the_goods,
        'price': product_info.price,
    }
    form = ProductForm(data=product_info_dict)
    if not request.POST:
        context = {
            'form': form,
            'product': product_info
        }
        return render(request, 'product_update_page.html', context=context)
    form = ProductForm(data=request.POST)
    if not form.is_valid():
        context = {
            'form': form,
            'product': product_info
        }
        return render(request, 'product_update_page.html', context=context)
    else:
        product_info.product_name = request.POST.get('product_name')
        product_info.product_description = request.POST.get('product_description')
        product_info.product_image = request.POST.get('product_image')
        product_info.category = request.POST.get('category')
        product_info.the_rest_of_the_goods = request.POST.get('the_rest_of_the_goods')
        product_info.price = request.POST.get('price')
        product_info.save()
        return redirect('product_detail', pk=product_info.pk)