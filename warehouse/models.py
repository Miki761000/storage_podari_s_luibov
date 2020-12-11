from django.db import models

from warehouse.validators import positive_number


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=250)

    # category_description = models.TextField(default='', blank=True)

    def __str__(self):
        return f'{self.category_name}'


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_code = models.CharField(max_length=100)
    product_name = models.CharField(max_length=500)
    product_quantity = models.IntegerField(default=0, blank=True, )  # calculation field
    product_delivery_price = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                                 blank=True)  # calculation field
    product_description = models.TextField(default='', blank=True)
    product_image = models.ImageField(
        upload_to='products',
        blank=True,
        null=True,
    )
    product_type = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}; {self.product_code}; {self.product_name};' \
               f'{self.product_quantity}; {self.product_delivery_price}; ' \
               f'{self.product_image}; {self.product_type};' \
               f'{self.product_description}'


class ProductAdditionalInformation(models.Model):
    product_code = models.CharField(max_length=100)
    product_quantity_add = models.IntegerField(
        validators=[positive_number],
        default=0,
        blank=True,
    )
    product_quantity_returned = models.IntegerField(
        validators=[positive_number],
        default=0,
        blank=True,
    )
    product_quantity_sale = models.IntegerField(
        validators=[positive_number],
        default=0,
        blank=True,
    )
    product_quantity_waste = models.IntegerField(
        validators=[positive_number],
        default=0,
        blank=True,
    )
    product_delivery_price_add = models.DecimalField(
        validators=[positive_number],
        max_digits=10,
        decimal_places=2,
        default=0,
        blank=True
    )
    product_add_date = models.DateField(auto_now=True)
    document = models.CharField(max_length=300, default='', blank=True)

    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
