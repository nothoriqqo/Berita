from django.contrib import admin
from django.urls import path, include

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler400, handler500

from . views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('blog.urls')),
    
    path('artikel/<int:id>/detail/', detail_artikel, name='detail_artikel'),
    
    path('', index, name='index'),
    path('about/',about, name='about'),
    
    path('login/',login, name='login'),
    path('logout/',logout_view, name='logout'),

    path('ckeditor/', include('ckeditor_uploader.urls'))

]
