from django import forms

from warehouse.forms.common import DisabledFormMixin
from warehouse.models import Product, ProductAdditionalInformation
from warehouse.validators import positive_number


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        class Meta:
            model = Product
            fields = '__all__'
            field_order = [
                'product_name',
                'product_code',
                'product_quantity',
                'product_type',
                'product_id',
            ]


class ProductAdditionalInformationForm(forms.ModelForm):
    class Meta:
        model = ProductAdditionalInformation
        fields = '__all__'
        # fields = {'product_code', 'product_quantity_add', 'product_quantity_returned',
        #           'product_quantity_sale', 'product_quantity_waste', 'product_delivery_price_add',
        #           'document', }
        # widgets = {'product': forms.HiddenInput}


class DeleteProductForm(ProductForm, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)
