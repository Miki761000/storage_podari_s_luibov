from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import TemplateView
from django.db import transaction

from accounts.forms import UserProfileForm, SignUpForm
from accounts.models import UserProfile
from accounts.tokens import account_activation_token

from django.urls import reverse_lazy
from django.views import generic as views

from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User


class UserProfileView(views.UpdateView):
    template_name = 'accounts/user_profile.html'
    form_class = UserProfileForm
    model = UserProfile
    success_url = reverse_lazy('current user profile')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)
        user = self.request.user \
            if pk is None \
            else User.objects.get(pk=pk)
        return user.userprofile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['profile_user'] = self.get_object().user

        return context


class SignInView(auth_views.LoginView):
    template_name = 'accounts/signin.html'


class RegisterView(TemplateView):
    template_name = 'accounts/signup.html'
    success_message = 'Great! You are already registered.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = SignUpForm()
        context['profile_form'] = UserProfileForm()
        return context

    @transaction.atomic
    def post(self, request):
        user_form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('index')

        context = {
            'user_form': SignUpForm(),
            'profile_form': UserProfileForm(),
        }

        return render(request, 'accounts/signup.html', context)


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


# def user_profile(request, pk=None):
#     user = request.user if pk is None else User.objects.get(pk=pk)
#     if request.method == 'GET':
#         context = {
#             'profile_user': user,
#             'profile': user.userprofile,
#             'form': UserProfileForm(),
#         }
#
#         return render(request, 'accounts/user_profile.html', context)
#     else:
#         form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
#         if form.is_valid():
#             form.save()
#             return redirect('current user profile')
#
#         return redirect('current user profile')
#
#
# def signup_user(request):
#     if request.method == 'GET':
#         context = {
#             'form': SignUpForm(),
#             'profile_form': UserProfileForm()
#         }
#
#         return render(request, 'accounts/signup.html', context)
#     else:
#         form = SignUpForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             user = form.save()
#             profile = UserProfile(
#                 user=user,
#             )
#             profile.save()
#
#             login(request, user)
#             return redirect('current user profile')
#             # return redirect('index')
#
#         context = {
#             'form': form,
#         }
#
#         return render(request, 'accounts/signup.html', context)
#
#
# def signout_user(request):
#     logout(request)
#     return redirect('index')
