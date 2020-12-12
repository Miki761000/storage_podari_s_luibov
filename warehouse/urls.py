from django.urls import path

from warehouse.views.index import IndexPage, get_private_file, get_public_file
from warehouse.views.category import CategoryCreateView, DeleteCategoryView, \
    UpdateCategoryView, CategoryListView
from warehouse.views.products import ProductCreateView, DeleteProductView, UpdateProductView, \
    add_quantity_product, details_product, list_product  # ProductListView,

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),

    path('list_category/', CategoryListView.as_view(), name='list category'),
    path('create_category/', CategoryCreateView.as_view(), name='create category'),
    path('category/edit/<int:pk>/', UpdateCategoryView.as_view(), name='edit category'),
    path('category/delete/<int:pk>/', DeleteCategoryView.as_view(), name='delete category'),

    # path('list_product/', ProductListView.as_view(), name='list product'),
    path('list_product/', list_product, name='list product'),
    path('create_product/', ProductCreateView.as_view(), name='create product'),
    path('product/edit/<int:pk>/', UpdateProductView.as_view(), name='edit product'),
    path('product/delete/<int:pk>/', DeleteProductView.as_view(), name='delete product'),
    path('product/details/<int:pk>/', details_product, name='details product'),
    path('add_quantity_product/<int:pk>/', add_quantity_product, name='add quantity product'),

    # path('', index, name='index'),
    # path('resources_private/<path:path_to_file>/', get_private_file, name='private file'),
    # path('resources_public/<path:path_to_file>/', get_public_file, name='public file'),

    # path('list_category/', list_category, name='list category'),
    # path('create_category/', create_category, name='create category'),
    # path('category/edit/<int:pk>/', edit_category, name='edit category'),
    # path('category/delete/<int:pk>/', delete_category, name='delete category'),
    # path('category/details/<int:pk>/', details_category, name='details category'),

    # path('create_product/', create_product, name='create product'),
    # path('product/edit/<int:pk>/', edit_product, name='edit product'),
    # path('product/delete/<int:pk>/', delete_product, name='delete product'),

]
