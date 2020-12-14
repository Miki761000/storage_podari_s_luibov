from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db.models.functions import Lower
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views
from django.views.generic import FormView, CreateView
from django.contrib.auth import mixins as auth_mixins

from accounts.decorators import user_required, superuser_required
from common.decorators import groups_required
from core.clean_up import clean_up_files
from warehouse.forms.common import FilterForm, extract_filter_values
from warehouse.forms.products import ProductForm, DeleteProductForm, ProductAdditionalInformationForm
from warehouse.models import Product, ProductAdditionalInformation
from warehouse.views.common import calculate_quantity_and_price


@method_decorator(login_required, name='dispatch')
class ProductCreateView(FormView):
    form_class = ProductForm
    template_name = 'product/product-create.html'
    success_url = reverse_lazy('list product')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class UpdateProductView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'product/product-edit.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        url = reverse_lazy('edit product', kwargs={'pk': self.object.id})
        url_list = reverse_lazy('list product')
        return url_list

    def form_valid(self, form):
        # old_image = self.get_object().image
        # if old_image:
        #     clean_up_files(old_image.path)
        form.save()
        return super().form_valid(form)


@method_decorator(groups_required(groups=['Super User']), name='dispatch')
class DeleteProductView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Product
    template_name = 'product/product-delete.html'
    success_url = reverse_lazy('list product')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


@login_required
# @superuser_required()
def details_product(request, pk):
    product = Product.objects.get(pk=pk)
    quantities = ProductAdditionalInformation.objects.all()

    product.product_quantity, product.product_delivery_price = calculate_quantity_and_price(product.product_code, product, quantities)

    context = {
        'product': product,
        'form': ProductForm(instance=product),
        'form_quantity': ProductAdditionalInformationForm(instance=product),
    }

    return render(request, 'product/product-details.html', context)


@login_required
def list_product(request):
    params = extract_filter_values(request.GET)
    order_by = 'product_name' if params['order'] == FilterForm.ORDER_ASC else '-product_name'
    products = Product.objects.filter(product_name__icontains=params['text']).order_by('product_name') | \
               Product.objects.filter(product_code__icontains=params['text']).order_by('product_name') | \
               Product.objects.filter(product_description__icontains=params['text']).order_by('product_name') | \
               Product.objects.filter(product_type__category_name__icontains=params['text']).order_by('product_name')

    for product in products:
        quantities = ProductAdditionalInformation.objects.all()
        product.product_quantity, product.product_delivery_price = calculate_quantity_and_price(product.product_code, product, quantities)

    items_per_page = 6
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

    context = {
        'products': products,
        'current_page': 'home',
        'filter_form': FilterForm(initial=params),
        'page_range': page_range,
        # 'can_delete': request.user.is_superuser == True
    }

    return render(request, 'product/product-list.html', context )


@login_required
# @superuser_required()
def add_quantity_product(request, pk):
    product = Product.objects.get(pk=pk)
    pr_code = product.product_code
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


from django import template
register = template.Library()


@register.filter
def sort_by(queryset, order):
    return queryset.order_by(order)


# @login_required
# # @superuser_required()
# def create_product(request):
#     if request.method == 'GET':
#         context = {
#             'form': ProductForm(),
#         }
#
#         return render(request, 'product/product-create.html', context)
#     else:
#         form = ProductForm(request.POST, request.FILES)
#         print(form)
#         if form.is_valid():
#             python = form.save()
#             python.save()
#             return redirect('index')
#
#
# @login_required
# # @superuser_required()
# def edit_product(request, pk):
#     product = Product.objects.get(pk=pk)
#
#     if request.method == 'GET':
#         context = {
#             'product': product,
#             'form': ProductForm(instance=product),
#         }
#
#         return render(request, 'product/product-edit.html', context)
#     else:
#         form = ProductForm(request.POST, request.FILES, instance=product)
#
#         if form.is_valid():
#             form.save()
#             return redirect('list product')
#
#         context = {
#             'product': product,
#             'form': form,
#         }
#
#         return render(request, 'product/product-edit.html', context)
#
#
# @user_required(Product)
# # @superuser_required()
# def delete_product(request, pk):
#     product = Product.objects.get(pk=pk)
#
#     if request.method == 'GET':
#         context = {
#             'product': product,
#             'form': DeleteProductForm(instance=product),
#         }
#
#         return render(request, 'product/product-delete.html', context)
#
#     else:
#         product.delete()
#         return redirect('index')
#

# @login_required
# # @superuser_required()
# def details_product(request, pk):
#     product = Product.objects.get(pk=pk)
#     quantities = ProductAdditionalInformation.objects.all()
#
#     product.product_quantity, product.product_delivery_price = calculate_quantity_and_price(pk, product, quantities)
#
#     context = {
#         'product': product,
#         'form': ProductForm(instance=product),
#         'form_quantity': ProductAdditionalInformationForm(instance=product),
#     }
#
#     return render(request, 'product/product-details.html', context)
#
#
# @login_required
# # @superuser_required()
# def list_product(request):
#     params = extract_filter_values(request.GET)
#     order_by = 'product_name' if params['order'] == FilterForm.ORDER_ASC else '-product_name'
#     products = Product.objects.filter(product_name__icontains=params['text']).order_by(order_by) | \
#                Product.objects.filter(product_code__icontains=params['text']).order_by(order_by) | \
#                Product.objects.filter(product_description__icontains=params['text']).order_by(order_by) | \
#                Product.objects.filter(product_type__category_name__icontains=params['text']).order_by(order_by)
#
#     for product in products:
#         quantities = ProductAdditionalInformation.objects.all()
#         product.product_quantity, product.product_delivery_price = calculate_quantity_and_price(product.id, product, quantities)
#
#     # context = {
#     #     'products': products,
#     #     'current_page': 'home',
#     #     'filter_form': FilterForm(initial=params),
#     #     # 'products': Product.objects.all(),
#     # }
#     #
#     # return render(request, 'product/product-list.html', context)
#
#     items_per_page = 10
#     paginator = Paginator(products, items_per_page)
#
#     try:
#         page = int(request.GET.get('page', '1'))
#     except:
#         page = 1
#
#     try:
#         products = paginator.page(page)
#     except(EmptyPage, InvalidPage):
#         products = paginator.page(1)
#
#     # Get the index of the current page
#     index = products.number - 1  # edited to something easier without index
#     # This value is maximum index of your pages, so the last page - 1
#     max_index = len(paginator.page_range)
#     # You want a range of 7, so lets calculate where to slice the list
#     start_index = index - 3 if index >= 3 else 0
#     end_index = index + 3 if index <= max_index - 3 else max_index
#     # Get our new page range. In the latest versions of Django page_range returns
#     # an iterator. Thus pass it to list, to make our slice possible again.
#     page_range = list(paginator.page_range)[start_index:end_index]
#
#     return render(request, 'product/product-list.html', {
#         'products': products,
#         'current_page': 'home',
#         'filter_form': FilterForm(initial=params),
#         'page_range': page_range,
#     })
#
#


# class ProductListView(views.ListView):
#     model = Product
#     template_name = 'product/product-list.html'
#     context_object_name = 'products'
#
#     def dispatch(self, request, *args, **kwargs):
#         params = extract_filter_values(request.GET)
#         self.order_by = params['order']
#         self.contains_text = params['text']
#         return super().dispatch(request, *args, **kwargs)
#
#     def get_queryset(self):
#         order_by = 'product_name' if self.order_by == FilterForm.ORDER_ASC else '-product_name'
#         result = self.model.objects.filter(product_name__icontains=self.contains_text).order_by(order_by) | \
#                self.model.objects.filter(product_code__icontains=self.contains_text).order_by(order_by) | \
#                self.model.objects.filter(product_description__icontains=self.contains_text).order_by(order_by) | \
#                self.model.objects.filter(product_type__category_name__icontains=self.contains_text).order_by(order_by)
#
#         return result
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filter_form'] = FilterForm(initial={
#             'order': self.order_by,
#             'text': self.contains_text
#         })
#
#         return context
#
#     for product in model.objects.all():
#         quantities = ProductAdditionalInformation.objects.all()
#         product_quantity, product_delivery_price = calculate_quantity_and_price(
#                 model.id, product, quantities)
