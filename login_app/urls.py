from django.urls import path
from . import views

urlpatterns = [
    path("", views.signin, name="Login"),
    path("home/", views.home, name="Home"),
    path("signup/", views.create_user, name="signup"),
    path("logout/", views.close_session, name="logout"),
    path("login/", views.signin, name="login")
]