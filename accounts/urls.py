from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken, obtain_auth_token
from .views import (
    AccountDetailProtectedView,
    AccountView,
    AccountSortedView,
    AccountDetailView,
)

urlpatterns = [
    path("login/", obtain_auth_token, name="login"),
    path("accounts/", AccountView.as_view()),
    path("accounts/newest/<int:num>/", AccountSortedView.as_view()),
    path("accounts/<pk>/", AccountDetailView.as_view()),
    path("accounts/<pk>/management/", AccountDetailProtectedView.as_view()),
]
