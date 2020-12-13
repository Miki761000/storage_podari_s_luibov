from django.urls import path, include

from accounts.views import UserProfileView, SignInView, SignOutView, RegisterView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', UserProfileView.as_view(), name='current user profile'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user profile'),
    path('signin/', SignInView.as_view(), name='signin user'),
    path('signup/', RegisterView.as_view(), name='signup user'),
    path('signout/', SignOutView.as_view(), name='signout user'),

    # path('profile/', user_profile, name='current user profile'),
    # path('profile/<int:pk>/', user_profile, name='user profile'),
    # path('signup/', signup_user, name='signup user'),
    # path('signout/', signout_user, name='signout user'),
]
