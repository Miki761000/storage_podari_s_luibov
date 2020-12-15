from django import dispatch
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import FormView, DeleteView, DetailView
from django.contrib.auth import mixins as auth_mixins
from django.views import generic as views

from common.decorators import groups_required
from warehouse.forms.category import CategoryForm, DeleteCategoryForm
from warehouse.models import Category, Product


@login_required
def details_category(request, pk):
    category = Category.objects.get(pk=pk)
    category_id = category.id
    product = Product.objects.filter(product_type=category_id)

    context = {
        'products': product,
        'category': category,
    }

    return render(request, 'category/category-detail.html', context)


@method_decorator(login_required, name='dispatch')
class CategoryListView(views.ListView):
    model = Category
    template_name = 'category/category-list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.order_by('category_name')


# @method_decorator(groups_required(groups=['Regular User', 'Super User']), name='dispatch')
@method_decorator(login_required, name='dispatch')
class CategoryCreateView(FormView):
    form_class = CategoryForm
    template_name = 'category/category-create.html'
    success_url = reverse_lazy('index')
    # groups = ['Super User', 'Active User']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class UpdateCategoryView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'category/category-edit.html'
    model = Category
    form_class = CategoryForm

    def get_success_url(self):
        url = reverse_lazy('edit category', kwargs={'pk': self.object.id})
        url_list = reverse_lazy('list category')
        return url_list

    def form_valid(self, form):
        # old_image = self.get_object().image
        # if old_image:
        #     clean_up_files(old_image.path)
        return super().form_valid(form)


@method_decorator(groups_required(groups=['Super User']), name='dispatch')
class DeleteCategoryView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Category
    template_name = 'category/category-delete.html'
    success_url = reverse_lazy('list category')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# @login_required
# def create_category(request):
#     if request.method == 'GET':
#         context = {
#             'form': CategoryForm(),
#         }
#
#         return render(request, 'category/category-create.html', context)
#     else:
#         form = CategoryForm(request.POST, request.FILES)
#         print(form)
#         if form.is_valid():
#             python = form.save()
#             python.save()
#             return redirect('index')


# @login_required
# # @superuser_required()
# def edit_category(request, pk):
#     category = Category.objects.get(pk=pk)
#
#     if request.method == 'GET':
#         context = {
#             'category': category,
#             'form': CategoryForm(instance=category),
#         }
#
#         return render(request, 'category/category-edit.html', context)
#     else:
#         form = CategoryForm(request.POST, instance=category)
#
#         if form.is_valid():
#             form.save()
#             return redirect('list category')
#
#         context = {
#             'category': category,
#             'form': form,
#         }
#
#         return render(request, 'category/category-edit.html', context)
#
#
# @user_required(Category)
# # @superuser_required()
# def delete_category(request, pk):
#     category = Category.objects.get(pk=pk)
#
#     if request.method == 'GET':
#         context = {
#             'category': category,
#             'form': DeleteCategoryForm(instance=category),
#         }
#
#         return render(request, 'category/category-delete.html', context)
#
#     else:
#         category.delete()
#         return redirect('index')
#
# @login_required
# # @superuser_required()
# def details_category(request, pk):
#     category = Category.objects.get(pk=pk)
#
#     context = {
#         'category': category,
#         'form': CategoryForm(),
#     }
#
#     return render(request, 'category/category-details.html', context)
#
#
# @login_required
# # @superuser_required()
# def list_category(request):
#     context = {
#         'categories': Category.objects.all(),
#     }
#
#     return render(request, 'category/category-list.html', context)

