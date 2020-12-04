from django import forms

from warehouse.forms.common import DisabledFormMixin
from warehouse.models import Category


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'
        field_order = ['category_name', 'category_id']


class DeleteCategoryForm(CategoryForm, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)

