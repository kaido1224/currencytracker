from django.contrib.auth import views as auth_views
from django.urls import path

from . import views as currency_views

app_name = "myapp"

urlpatterns = [
    path('', currency_views.IndexView.as_view(), name='index'),

    path('login/', currency_views.LoginView.as_view(), name='login'),
    path('logout/', currency_views.LogoutView.as_view(), name='logout'),
]
