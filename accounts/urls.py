from django.urls import path, include

from accounts.views import signup_user, signout_user, user_profile

urlpatterns = [
    # path('signin/', LoginView.as_view(template_name='registration/signup.html'), name='signin user', ),
    path('', include('django.contrib.auth.urls')),
    path('profile/', user_profile, name='current user profile'),
    path('profile/<int:pk>/', user_profile, name='user profile'),
    path('signup/', signup_user, name='signup user'),
    path('signout/', signout_user, name='signout user'),
]