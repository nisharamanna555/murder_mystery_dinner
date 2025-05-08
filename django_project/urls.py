from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("home/", login_required(TemplateView.as_view(template_name="home.html")), name="home"),
    path("admin/", admin.site.urls),
]
