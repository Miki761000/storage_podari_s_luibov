from django.contrib import admin

from warehouse.models import Category, Product, ProductAdditionalInformation


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    list_filter = ('category_name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_code', 'product_name', 'product_type', 'product_image', )
    list_filter = ('product_type',)


class ProductAdditionalInformationAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'id', 'product_quantity_add', 'product_quantity_returned', 'product_quantity_sale',
                    'product_quantity_waste', 'product_delivery_price_add', 'product_add_date', 'document',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAdditionalInformation, ProductAdditionalInformationAdmin)
