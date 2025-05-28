from django.contrib import admin
from django.urls import path
from My_Spider.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('account/', account_view, name='account'),
    path('diario/', diario_view, name='diario'),
    path('logout/', logout_view, name='logout'),
    path('cerca', cerca_view, name='cerca'),
    path('biblioteca/', biblioteca_view, name='biblioteca'),
    path('add_spider/', add_spider, name='add_spider'),
]