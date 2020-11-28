from django.contrib import admin

from warehouse.models import Category, Product, ProductAdditionalInformation


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name')
    list_filter = ('category_name', )


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_code', 'product_name', 'product_type', 'product_description', 'product_image' )
    list_filter = ('product_code', 'product_type', 'product_name',)


class ProductAdditionalInformationAdmin(ProductAdmin):
    list_display = ('product_id', 'product_quantity_add', 'product_quantity_returned', 'product_delivery_price_add', 'product_add_date' )
    list_filter = ('product_quantity_add',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAdditionalInformation, ProductAdditionalInformationAdmin)
