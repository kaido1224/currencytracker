import json

from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.views import View
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView
from django.views.generic import RedirectView

from myapp import forms

from myapp.models import Currency

from pycountry import countries
from pycountry import historic_countries


class AddEntryView(LoginRequiredMixin, View):
    t = "add_entry.html"

    def get_entry_info(self, id):
        """Attempt to get entry based on ID specified. If there was an error, this will return None.
        """
        try:
            results = Currency.objects.get(pk=id)
        except Currency.DoesNotExist:
            return None

        return results

    def get(self, request, id=None):
        ctx = {}

        # If editing an existing entry.
        if id:
            entry = self.get_entry_info(id)

            if not entry:
                messages.error(request, "Invalid entry specified.")
                return redirect("myapp:collection")

            ctx["form"] = forms.EntryForm(instance=entry, initial={"book": entry.book})
            ctx["entry"] = entry

        else:
            ctx["form"] = forms.EntryForm()

        return render(request, self.t, ctx)

    def post(self, request, id=None):
        ctx = {}

        # If editing an existing entry
        if id:
            entry = self.get_entry_info(id)
            ctx["entry"] = entry

            if not entry:
                messages.error(request, "Invalid entry specified.")
                return redirect("myapp:collection")

            form = forms.EntryForm(request.POST, instance=entry)
        else:
            form = forms.EntryForm(request.POST)

        if not form.is_valid():
            messages.error(request, "Form is invalid, make appropriate corrections and try again.")
            ctx["form"] = form
            return render(request, self.t, ctx)

        form.save()

        if id:
            message = "Updated entry successfully."
        else:
            message = "Created new entry successfully."

        messages.success(request, message)

        # Redirect to appropriate page based on button clicked.
        if "_create_another" in request.POST:
            return redirect("myapp:add_entry")
        else:
            return redirect("myapp:collection")


class CollectionView(LoginRequiredMixin, View):
    t = "collection.html"

    def get(self, request):
        ctx = {}

        currency = Currency.objects.all()

        results = []

        for line in currency:
            line_info = {}
            line_info["id"] = line.id
            line_info["book"] = line.book
            line_info["page"] = line.page
            line_info["row"] = line.page
            line_info["column"] = line.column
            line_info["currency"] = line.currency
            line_info["value"] = line.value
            line_info["type"] = line.type

            # Hard-coded because CS is used multiple times for different countries.
            if line.country == "CS":
                country_code = "Czechoslovakia"
            elif line.country == "MB":
                country_code == "Serbia and Montenegro"
            elif line.country == "CE":
                # Multiple countries use this as their currency.
                country_code = "Eastern Carribean Islands"
            else:
                try:
                    country_code = countries.get(alpha_2=line.country).name
                except Exception:
                    country_code = None

                if not country_code:
                    try:
                        country_code = historic_countries.get(alpha_2=line.country).name
                    except Exception:
                        country_code = line.country

            line_info["country"] = country_code
            results.append(line_info)

        ctx["results"] = results

        return render(request, self.t, ctx)


class DeleteEntryView(LoginRequiredMixin, View):
    def post(self, request, id):
        try:
            Currency.objects.get(pk=id).delete()

            messages.success(request, "Successfully deleted entry.")

        except Currency.DoesNotExist:
            messages.error(request, "Failed to delete entry.")

        return redirect("myapp:collection")


class IndexView(LoginRequiredMixin, View):
    t = "index.html"

    def get(self, request):
        ctx = {}

        coin_countries = (Currency.objects.filter(type="Coin").distinct()
                                  .values_list("country", flat=True))
        ctx["coin_countries"] = json.dumps(list(coin_countries))

        return render(request, self.t, ctx)


class LoginView(FormView):
    """Basic login screen.
    """
    success_url = "/"
    form_class = forms.LoginForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'login.html'

    def get_form_kwargs(self):
        """The kwargs passed to the form constructor.

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
