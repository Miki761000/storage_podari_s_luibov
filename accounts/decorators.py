from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect


def user_required(model_class, methods=None):
    if methods is None:
        methods = ['GET', 'POST']

    def decorator(view_func):
        def wrapper(request, pk, *args, **kwargs):
            model_obj = model_class.objects.get(pk=pk)

            if request.method not in methods or model_obj.user.user_id == request.user.id:
                return view_func(request, pk, *args, **kwargs)
            return redirect('login')

        return wrapper

    return decorator


def superuser_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME,
                   login_url='signup user'):
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