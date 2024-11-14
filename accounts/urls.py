from django.urls import path

from accounts import views

urlpatterns = [
    path(
        "accounts/singup", views.AccountCrateView.as_view(), 
        name='singup'
    ),
] 