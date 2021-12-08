from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UsernameField


class LoginForm(AuthenticationForm):
    username = UsernameField(max_length=254, widget=forms.TextInput(attrs={'autofocus':
                                                                           'staybasedyafeelme'}))
