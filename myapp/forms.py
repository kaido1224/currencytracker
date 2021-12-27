import pycountry

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UsernameField

from myapp import models


class BookForm(forms.ModelForm):
    rows_per_page = forms.IntegerField(label="Rows Per Page", required=False, min_value=0)
    columns_per_row = forms.IntegerField(label="Columns Per Row", required=False, min_value=0)
    pages = forms.IntegerField(required=False, min_value=0)

    class Meta:
        model = models.Book
        exclude = ["id", "created_ts", "updated_ts"]


class EntryForm(forms.ModelForm):
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
            ("AA", "Central Africa CFA"),
            ("CE", "Eastern Carribean Islands"),
            ("MB", "Serbia and Montenegro"),
            ("WA", "West Africa CFA")
        ]

        countries.extend(custom_countries)

        countries.sort()

        super().__init__(*args, **kwargs)
        self.fields["country"] = forms.ChoiceField(choices=countries, required=False)

    class Meta:
        model = models.Currency
        exclude = ["id", "created_ts", "updated_ts"]


class LoginForm(AuthenticationForm):
    username = UsernameField(max_length=254, widget=forms.TextInput())
