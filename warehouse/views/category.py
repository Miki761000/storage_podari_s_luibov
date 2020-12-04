from django import dispatch
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import FormView, DeleteView

from accounts.decorators import user_required, superuser_required
from common.decorators import groups_required
from common.view_mixins import GroupRequiredMixin, UserRequiredMixin
from warehouse.forms.category import CategoryForm, DeleteCategoryForm
from warehouse.forms.common import extract_filter_values
from warehouse.models import Category


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


# @method_decorator(groups_required(groups=['Regular User', 'Super User']), name='dispatch')
@method_decorator(login_required, name='dispatch')
# class CategoryEditView(GroupRequiredMixin, LoginRequiredMixin, FormView):
class CategoryEditView(FormView):
    form_class = CategoryForm
    template_name = 'category/category-edit.html'
    success_url = reverse_lazy('list category')
    # groups = ['User']

    def get_form_kwargs(self):
        kwargs = super(CategoryEditView,self).get_form_kwargs()
        kwargs.update(self.kwargs)
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DeleteCategoryView(DeleteView):
    model = Category
    success_url = reverse_lazy('category/category-delete.html')

    def get_queryset(self, *args, **kwargs):
        return DeleteCategoryForm.objects.filter(category_id=self.kwargs['pk'])

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



@login_required
# @superuser_required()
def details_category(request, pk):
    category = Category.objects.get(pk=pk)

    context = {
        'category': category,
        'form': CategoryForm(),
    }

    return render(request, 'category/category-details.html', context)


@login_required
# @superuser_required()
def list_category(request):
    context = {
        'categories': Category.objects.all(),
    }

    return render(request, 'category/category-list.html', context)

