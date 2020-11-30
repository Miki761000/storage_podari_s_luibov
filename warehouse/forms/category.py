from django import forms

from warehouse.forms.common import DisabledFormMixin
from warehouse.models import Category


class CategoryForm(forms.ModelForm):

    # def clean_time(self):
    #     minutes = self.cleaned_data['time']
    #     if minutes <= 0:
    #         raise ValidationError(f'Minutes should be a positive number. Now they are {minutes}')
    #     return minutes

    class Meta:
        model = Category
        fields = '__all__'


class DeleteCategoryForm(CategoryForm, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)