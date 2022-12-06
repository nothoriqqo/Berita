from django.contrib import admin
from django.urls import path, include

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler400, handler500

from . views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('dashboard/', include('blog.urls')),
    path('about/',about, name='about'),
    path('login/',login, name='login'),
    path('register/',register, name='register'),
]
