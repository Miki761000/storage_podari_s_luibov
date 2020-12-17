from django import forms

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
        exclude = ['product']
        fields = '__all__'