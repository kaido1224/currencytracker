from functools import wraps

from django.contrib import messages
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect

from myapp.utils import is_read_only_user


def write_perms_required(view_function):
    """Don't allow read only users to access this view.
    """
    @wraps(view_function)
    def _wrapped_view(request, *args, **kwargs):
        user = request.user

        # If user isn't authenticated, send them to the login page.
        if not request.user.is_authenticated:
            return redirect_to_login("/")

        authorized_user = not is_read_only_user(user)

        # If they are a read_only user, redirect them to the home page.
        if not authorized_user:
            messages.error(request, "You don't have permission to view this page.")
            return redirect("myapp:index")

        # If they're configured as expected, send them along.
        elif authorized_user:
            return view_function(request, *args, **kwargs)

    return _wrapped_view
