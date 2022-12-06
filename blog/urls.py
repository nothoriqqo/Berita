from blog.models import *
from django.urls import path 

from blog.views import *
urlpatterns = [
    path('', artikel_list, name='table_artikel'),
    path('users', users, name='table_users'),
    path('artikel_add', artikel_add, name='artikel_add'),
    path('artikel/update/<str:id>', artikel_update, name='artikel_update'),
    path('artikel/delete/<str:id>', artikel_delete, name='artikel_delete'),
    path('artikel/detail/<str:id>', artikel_detail, name='artikel_detail'),
]