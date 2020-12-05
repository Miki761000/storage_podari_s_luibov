from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from accounts.forms import UserProfileForm, SignUpForm
from accounts.models import UserProfile
from accounts.tokens import account_activation_token


def user_profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'profile_user': user,
            'profile': user.userprofile,
            'form': UserProfileForm(),
        }

        return render(request, 'accounts/user_profile.html', context)
    else:
        form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('current user profile')

        return redirect('current user profile')


def signup_user(request):
    if request.method == 'GET':
        context = {
            'form': SignUpForm(),
        }

        return render(request, 'accounts/signup.html', context)
    else:
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.save()
            profile = UserProfile(
                user=user,
            )
            profile.save()

            login(request, user)
            return redirect('current user profile')
            # return redirect('index')

        context = {
            'form': form,
        }

        return render(request, 'accounts/signup.html', context)


def signout_user(request):
    logout(request)
    return redirect('index')
