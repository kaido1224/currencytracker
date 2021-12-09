

from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.views import View
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView
from django.views.generic import RedirectView

from myapp.forms import LoginForm


class CollectionView(LoginRequiredMixin, View):
    t = "collection.html"

    def get(self, request):
        ctx = {}
        return render(request, self.t, ctx)


class IndexView(LoginRequiredMixin, View):
    t = "index.html"

    def get(self, request):
        ctx = {}
        return render(request, self.t, ctx)


class LoginView(FormView):
    """Basic login screen.
    """
    success_url = "/"
    form_class = LoginForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'login.html'

    def get_form_kwargs(self):
        """The kwargs that will get passed to the form constructor.

        Inherted from `FormMixin`.
        """
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    @method_decorator(sensitive_post_parameters("password"))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "Incorrect username or password.")
        return super().form_invalid(form)

    def get_success_url(self):
        redirect_to = self.request.GET.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, allowed_hosts=self.request.get_host()):
            redirect_to = self.success_url
        return redirect_to


class LogoutView(RedirectView):
    """Provides users the ability to logout.
    """
    url = "/login"

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
