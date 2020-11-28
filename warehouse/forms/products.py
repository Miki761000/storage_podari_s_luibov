from django import forms

from warehouse.forms.common import DisabledFormMixin
from warehouse.models import Product, ProductAdditionalInformation
from warehouse.validators import positive_number


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ProductAdditionalInformationForm(forms.ModelForm):
    class Meta:
        model = ProductAdditionalInformation
        fields = '__all__'
        # exclude = ('product', )


class DeleteProductForm(ProductForm, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)
