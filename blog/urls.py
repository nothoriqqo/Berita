from blog.models import *
from django.urls import path 

from blog.views import *
urlpatterns = [
    path('', artikel_list, name='table_artikel'),
    path('users', users, name='table_users'),
    path('artikel_add', artikel_add, name='artikel_add'),
    path('update/<int:id>', artikel_update, name='artikel_update'),
    path('delete/<int:id>', artikel_delete, name='artikel_delete'),
    path('detail/<int:id>', artikel_detail, name='artikel_detail'),
]