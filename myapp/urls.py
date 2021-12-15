from django.contrib.auth import views as auth_views
from django.urls import path

from . import views as currency_views

app_name = "myapp"

urlpatterns = [
    path('', currency_views.IndexView.as_view(), name='index'),
    path('collection', currency_views.CollectionView.as_view(), name="collection"),
    path('collection/add', currency_views.AddEntryView.as_view(), name="add_entry"),
    path('collection/delete/<int:id>', currency_views.DeleteEntryView.as_view(), name="delete_entry"),
    path('collection/edit/<int:id>', currency_views.AddEntryView.as_view(), name="edit_entry"),

    # Authorization pages.
    path('login/', currency_views.LoginView.as_view(), name='login'),
    path('logout/', currency_views.LogoutView.as_view(), name='logout'),
]
