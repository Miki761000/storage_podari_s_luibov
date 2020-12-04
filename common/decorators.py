from django.http import HttpResponse


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