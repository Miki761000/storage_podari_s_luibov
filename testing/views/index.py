from django.urls import reverse_lazy
from django.views.generic import FormView

from testing.forms.category import CategoryForm


class CategoryCreateView(FormView):
    form_class = CategoryForm
    template_name = 'testing/category/index.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)