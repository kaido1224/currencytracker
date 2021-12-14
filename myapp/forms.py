import pycountry

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UsernameField

from myapp import models


class CreateEntryForm(forms.ModelForm):
    book = forms.ModelChoiceField(models.Book.objects.all(), required=True,
                                  to_field_name='description')

    def __init__(self, *args, **kwargs):
        countries = [(country.alpha_2, country.name) for country in pycountry.countries]

        countries.insert(0, ("", "-" * 9))

        historic = [(country.alpha_2, country.name) for country in pycountry.historic_countries if
                    not country.name == "Serbia and Montenegro"]

        countries.extend(historic)

        # These are non-iso coded countries.
        custom_countries = [
            ("CE", "Eastern Carribean Islands"),
            ("MB", "Serbia and Montenegro")
        ]

        countries.extend(custom_countries)

        countries.sort()

        super().__init__(*args, **kwargs)
        self.fields["country"] = forms.ChoiceField(choices=countries)

    class Meta:
        model = models.Currency
        exclude = ["id", "created_ts", "updated_ts"]


class LoginForm(AuthenticationForm):
    username = UsernameField(max_length=254, widget=forms.TextInput())
