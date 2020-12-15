from django.urls import path

from testing.views.index import CategoryCreateView

urlpatterns = [
    path('categories/', CategoryCreateView.as_view(), name='categories'),
]