"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from pickle import NEXT_BUFFER
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    # for any routes with polling/, let the urls file in polling handle them
    path("", include("blogging.urls")),
    path("polling/", include("polling.urls")),
    path('admin/', admin.site.urls),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
]
