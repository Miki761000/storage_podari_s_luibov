from typing import List, Any, Tuple

from django.db import models


# Create your models here.


# class Warehouse(models.Model):
#     title = models.CharField(max_length=30)
#     image_url = models.URLField()
#     description = models.TextField()
#     ingredients = models.CharField(max_length=250)
#     time = models.IntegerField()
#
#     def __str__(self):
#         return f'{self.title}; {self.time}; {self.ingredients}; {self.description}; {self.image_url}'
#

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=250)
    # category_description = models.TextField(default='', blank=True)

    def __str__(self):
        return f'{self.category_name}'
    # return f'{self.category_name}; {self.category_description}'

#
# class Product(models.Model):
#     product_id = models.AutoField(primary_key=True)
#     product_code = models.CharField(max_length=100)
#     product_name = models.CharField(max_length=500)
#     product_quantity = models.IntegerField(default=0, blank=True)  # calculation field
#     product_delivery_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)  # calculation field
#     product_description = models.TextField(default='', blank=True)
#     product_image = models.ImageField(
#         # upload_to='public/products',
#         upload_to='products',
#         blank=True,
#         null=True,
#     )
#
#     product_type = models.ForeignKey(Category, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.product_code}; {self.product_name}; {self.product_description};' \
#                f' {self.product_image}; {self.product_type}'
#
#
# class ProductAdditionalInformation(models.Model):
#     product_quantity_add = models.IntegerField(default=0, blank=True)
#     product_quantity_returned = models.IntegerField(default=0, blank=True)
#     product_delivery_price_add = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)
#     product_add_date = models.DateField(auto_now=True)
#
#     product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
#
