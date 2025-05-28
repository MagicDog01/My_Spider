"""
URL configuration for My_Spider_X project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from My_Spider.views import login_view, home_view, signup_view, account_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", login_view, name="login"),
    path('', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('account/', account_view, name='account'),
    path ('logout/', logout_view, name='logout'),
]
