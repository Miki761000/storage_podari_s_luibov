from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.decorators import user_required, superuser_required
from warehouse.forms.category import CategoryForm, DeleteCategoryForm
from warehouse.models import Category


@login_required
# @superuser_required()
def create_category(request):
    if request.method == 'GET':
        context = {
            'form': CategoryForm(),
        }

        return render(request, 'category/category-create.html', context)
    else:
        form = CategoryForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            python = form.save()
            python.save()
            return redirect('index')


@login_required
# @superuser_required()
def edit_category(request, pk):
    category = Category.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'category': category,
            'form': CategoryForm(instance=category),
        }

        return render(request, 'category/category-edit.html', context)
    else:
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            form.save()
            return redirect('list category')

        context = {
            'category': category,
            'form': form,
        }

        return render(request, 'category/category-edit.html', context)


@user_required(Category)
# @superuser_required()
def delete_category(request, pk):
    category = Category.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'category': category,
            'form': DeleteCategoryForm(instance=category),
        }

        return render(request, 'category/category-delete.html', context)

    else:
        category.delete()
        return redirect('index')


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

