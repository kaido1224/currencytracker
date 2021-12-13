from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UsernameField

from myapp import models


class CreateEntryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        books = models.Book.objects.all()

        book_choices = [(b.description, b.description) for b in books]

        if len(book_choices) > 1:
            book_choices.insert(0, ("", "-" * 9))

        super().__init__(*args, **kwargs)
        self.fields["book"] = forms.ChoiceField(choices=book_choices)

#     page = models.IntegerField(null=True, default=None)
#     row = models.IntegerField(null=True, default=None)
#     column = models.IntegerField(null=True, default=None)
#     currency = models.CharField(max_length=100, blank=True, default="")
#     value = models.IntegerField(null=True, default=None)
#     type = models.CharField(max_length=4, choices=TYPE_CHOICES)
#     country = models.CharField(max_length=2, blank=True, default="")

    class Meta:
        model = models.Currency
        exclude = ["id", "created_ts", "updated_ts"]


class LoginForm(AuthenticationForm):
    username = UsernameField(max_length=254, widget=forms.TextInput())
