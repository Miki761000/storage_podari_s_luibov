from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.decorators import user_required, superuser_required
from warehouse.forms.common import FilterForm, extract_filter_values
from warehouse.forms.products import ProductForm, DeleteProductForm, ProductAdditionalInformationForm
from warehouse.models import Product, Category, ProductAdditionalInformation
from warehouse.views.common import calculate_quantity_and_price


@login_required
# @superuser_required()
def create_product(request):
    if request.method == 'GET':
        context = {
            'form': ProductForm(),
        }

        return render(request, 'product/product-create.html', context)
    else:
        form = ProductForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            python = form.save()
            python.save()
            return redirect('index')


@login_required
# @superuser_required()
def edit_product(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'product': product,
            'form': ProductForm(instance=product),
        }

        return render(request, 'product/product-edit.html', context)
    else:
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            return redirect('list product')

        context = {
            'product': product,
            'form': form,
        }

        return render(request, 'product/product-edit.html', context)


@user_required(Category)
# @superuser_required()
def delete_product(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'product': product,
            'form': DeleteProductForm(instance=product),
        }

        return render(request, 'product/product-delete.html', context)

    else:
        product.delete()
        return redirect('index')


@login_required
# @superuser_required()
def details_product(request, pk):
    product = Product.objects.get(pk=pk)
    quantities = ProductAdditionalInformation.objects.all()

    product.product_quantity, product.product_delivery_price = calculate_quantity_and_price(pk, product, quantities)

    context = {
        'product': product,
        'form': ProductForm(instance=product),
        'form_quantity': ProductAdditionalInformationForm(instance=product),
    }

    return render(request, 'product/product-details.html', context)


@login_required
# @superuser_required()
def list_product(request):
    params = extract_filter_values(request.GET)
    order_by = 'product_name' if params['order'] == FilterForm.ORDER_ASC else '-product_name'
    products = Product.objects.filter(product_name__icontains=params['text']).order_by(order_by) | \
               Product.objects.filter(product_code__icontains=params['text']).order_by(order_by) | \
               Product.objects.filter(product_description__icontains=params['text']).order_by(order_by) | \
               Product.objects.filter(product_type__category_name__icontains=params['text']).order_by(order_by)

    for product in products:
        quantities = ProductAdditionalInformation.objects.all()
        product.product_quantity, product.product_delivery_price = calculate_quantity_and_price(product.product_id, product, quantities)

    context = {
        'products': products,
        'current_page': 'home',
        'filter_form': FilterForm(initial=params),
        # 'products': Product.objects.all(),
    }

    return render(request, 'product/product-list.html', context)


@login_required
# @superuser_required()
def add_quantity_product(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'product': product,
            'form_quantity': ProductAdditionalInformationForm(),
        }
        return render(request, 'product/product-add-quantity.html', context)
    else:
        form_quantity = ProductAdditionalInformationForm(request.POST)

        if form_quantity.is_valid():

            quantity = form_quantity.save()
            quantity.product = product
            form_quantity.save()
            return redirect('list product')

        context = {
            'product': product,
            'form_quantity': form_quantity,
        }

    return render(request, 'product/product-add-quantity.html', context)
