from django import forms
from django.db import models

from warehouse.forms.common import DisabledFormMixin
from warehouse.models import Product, ProductAdditionalInformation


class ProductForm(forms.ModelForm):
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
        product_code = forms.CharField(disabled=True)


class ProductAdditionalInformationForm(forms.ModelForm):
    class Meta:
        model = ProductAdditionalInformation
        fields = '__all__'
        exclude = ['product']


class DeleteProductForm(ProductForm, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)


