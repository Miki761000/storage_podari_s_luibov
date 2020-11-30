from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, InvalidPage
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

    # context = {
    #     'products': products,
    #     'current_page': 'home',
    #     'filter_form': FilterForm(initial=params),
    #     # 'products': Product.objects.all(),
    # }
    #
    # return render(request, 'product/product-list.html', context)

    items_per_page = 10
    paginator = Paginator(products, items_per_page)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products = paginator.page(1)

    # Get the index of the current page
    index = products.number - 1  # edited to something easier without index
    # This value is maximum index of your pages, so the last page - 1
    max_index = len(paginator.page_range)
    # You want a range of 7, so lets calculate where to slice the list
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    # Get our new page range. In the latest versions of Django page_range returns
    # an iterator. Thus pass it to list, to make our slice possible again.
    page_range = list(paginator.page_range)[start_index:end_index]

    return render(request, 'product/product-list.html', {
        'products': products,
        'current_page': 'home',
        'filter_form': FilterForm(initial=params),
        'page_range': page_range,
    })


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
