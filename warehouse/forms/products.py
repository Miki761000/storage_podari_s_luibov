from django import forms

from warehouse.forms.common import DisabledFormMixin
from warehouse.models import Product, ProductAdditionalInformation


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    # def clean_product_additional_information(self):
    #     product_quantity_add = self.cleaned_data.get('product_quantity_add', False)
    #     product_quantity_returned = self.cleaned_data.get('product_quantity_returned', False)
    #     product_delivery_price_add = self.cleaned_data.get('product_delivery_price_add', False)


class ProductAdditionalInformationForm(forms.ModelForm):
    class Meta:
        model = ProductAdditionalInformation
        fields = '__all__'
        exclude = ('product',)

    # def clean_time(self):
    #     minutes = self.cleaned_data['time']
    #     if minutes <= 0:
    #         raise ValidationError(f'Minutes should be a positive number. Now they are {minutes}')
    #     return minutes


class DeleteProductForm(ProductForm, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)
