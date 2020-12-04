from django.urls import path

from warehouse.views.index import index, get_private_file, get_public_file
from warehouse.views.category import list_category, details_category, CategoryCreateView, CategoryEditView, \
    DeleteCategoryView
from warehouse.views.products import list_product, create_product, edit_product, delete_product, details_product, \
    add_quantity_product

urlpatterns = [
    path('', index, name='index'),

    # path('resources_private/<path:path_to_file>/', get_private_file, name='private file'),
    # path('resources_public/<path:path_to_file>/', get_public_file, name='public file'),

    path('list_category/', list_category, name='list category'),
    # path('create_category/', create_category, name='create category'),
    path('create_category/', CategoryCreateView.as_view(), name='create category'),
    # path('category/edit/<int:pk>/', edit_category, name='edit category'),
    path('category/edit/<int:pk>/', CategoryEditView.as_view(), name='edit category'),
    # path('category/delete/<int:pk>/', delete_category, name='delete category'),
    path('category/delete/<int:pk>/', DeleteCategoryView.as_view(), name='delete category'),
    path('category/details/<int:pk>/', details_category, name='details category'),

    path('list_product/', list_product, name='list product'),
    path('create_product/', create_product, name='create product'),
    path('product/edit/<int:pk>/', edit_product, name='edit product'),
    path('product/delete/<int:pk>/', delete_product, name='delete product'),
    path('product/details/<int:pk>/', details_product, name='details product'),

    path('add_quantity_product/<int:pk>/', add_quantity_product, name='add quantity product'),

]
