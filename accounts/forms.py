from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from accounts.models import UserProfile
from common.CssFormMixin import CssFormMixin


class SignUpForm(UserCreationForm, CssFormMixin):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture',)