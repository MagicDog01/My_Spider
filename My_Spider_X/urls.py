from django.contrib import admin
from django.urls import path
from My_Spider.views import *
from My_Spider import views
from django.conf import settings
from django.conf.urls.static import static
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
    path('delete_spider/<int:spider_id>/', delete_spider, name='delete_spider'),
    path('crea_evento/<int:spider_id>/', views.crea_evento_view, name='crea_evento'),
    path('lista_eventi/<int:spider_id>/', views.lista_eventi_view, name='lista_eventi'),
    path('elimina_evento/<int:pk>/', views.elimina_evento, name='elimina_evento'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])