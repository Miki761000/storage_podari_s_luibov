from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from accounts.models import UserProfile
from common.CssFormMixin import CssFormMixin


class SignUpForm(UserCreationForm, CssFormMixin):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-Mail'}),
            'password1': forms.TextInput(attrs={'placeholder': 'password'}),
            'password2': forms.TextInput(attrs={'placeholder': 'confirm password'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture',)