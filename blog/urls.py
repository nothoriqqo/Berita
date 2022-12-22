from blog.models import *
from django.urls import path 

from blog.views import *
urlpatterns = [
    path('dashboard', dashboard, name="dashboard"),
    path('', artikel_list, name='table_artikel'),
    path('users', users, name='users'),
    path('artikel_add', artikel_add, name='artikel_add'),
    path('artikel/update/<str:id>', artikel_update, name='artikel_update'),
    path('artikel/delete/<str:id>', artikel_delete, name='artikel_delete'),
    path('artikel/detail/<str:id>', artikel_detail, name='artikel_detail'),
    path('user/detail/<str:id>', user_detail, name='user_detail'),

    path('user/edit/<str:id>', edit_user, name='edit_user'),
    
    
]