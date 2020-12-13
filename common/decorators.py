from django.http import HttpResponse
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.admin.views.decorators import user_passes_test

def groups_required(groups=[]):
    groups_set = set(groups)

    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)

            # ако ги напишем wrapper(*args, **kwargs): request, ще отиде като args[0]
            user = request.user
            raw_groups = user.groups.all()
            # raw_groups = user.groups.only('name') # което за групите е същато като горното
            user_groups = set([group.name for group in raw_groups])

            if user_groups.intersection(groups_set):
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized')

        return wrapper

    return decorator


def superuser_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME,
                   login_url='account_login_url'):
    """
    Decorator for views that checks that the user is logged in and is a
    superuser, redirecting to the login page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator