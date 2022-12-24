
from pyexpat.errors import messages
from turtle import title
from django.shortcuts import render, redirect
from blog.models import Artikel, Kategori, Users
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth.models import User

import requests




def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False

@login_required
@user_passes_test(is_operator)
def artikel_list(request):
    template_name = 'back/table_artikel.html'
    artikel_list = Artikel.objects.all()
    context = {
        'title ' : 'halaman awal artikel',
        'artikel':artikel_list
    }
    return render(request, template_name, context)
@login_required
@user_passes_test(is_operator)
def dashboard(request):
    template_name = 'back/base.html'
    context = {
        'title' : 'dashboard',
        'dashboard' : dashboard
    }
    return render(request, template_name, context)
@login_required
@user_passes_test(is_operator)
def users(request):
    users = User.objects.all()
    template_name = 'back/table_users.html'
    context = {
        'title' : 'halaman user',
        'users' : users
    }
    return render(request, template_name, context)
@login_required
@user_passes_test(is_operator)
def edit_user(request, id):
    template_name = 'back/edit_user.html'
    get_user = User.objects.get(id=id)
    if request.method == "POST":
        input_username = request.POST.get('username')
        input_password = request.POST.get('password')
        input_first_name = request.POST.get('first name')
        input_last_name = request.POST.get('last name')

        get_user.username = input_username
        get_user.password = input_password
        get_user.first_name = input_first_name
        get_user.last_name = input_last_name
        get_user.save()
        return redirect(User)
    context = {
        'title ' : 'halaman tambah User',
        'get_user': get_user,
    }
    return render(request, template_name, context)
@login_required
@user_passes_test(is_operator)
def artikel_add(request):
    template_name = 'back/artikel_add.html'
    kategoris = Kategori.objects.all()
    if request.method == "POST":
        input_nama = request.POST.get('nama')
        input_kategori = request.POST.get('kategori')
        input_judul = request.POST.get('judul')
        input_body = request.POST.get('body')
        input_date = request.POST.get('date')

        get_kategori= Kategori.objects.get(nama=input_kategori)

        Artikel.objects.create(
        nama = input_nama,
        kategori = get_kategori,
        judul = input_judul,
        body = input_body,
        date = input_date,
        )
        return redirect(artikel_list)
    context = {
        'title ' : 'halaman tambah artikel',
        'kategori' : kategoris
    }
    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator)
def artikel_update(request, id):
    template_name = 'back/artikel_add.html'
    kategori = Kategori.objects.all()
    get_artikel = Artikel.objects.get(id=id)
    if request.method == "POST":
        input_nama = request.POST.get('nama')
        input_kategori = request.POST.get('kategori')
        input_judul = request.POST.get('judul')
        input_body= request.POST.get('body')
        input_date= request.POST.get('date')

        get_kategori = Kategori.objects.get(nama=input_kategori)

        get_artikel.nama = input_nama
        get_artikel.judul = input_judul
        get_artikel.body = input_body
        get_artikel.date = input_date
        get_artikel. kategori = get_kategori
        get_artikel.save()
        return redirect(artikel_list)
    context = {
        'title ' : 'halaman tambah Artikel',
        'kategori' : kategori,
        'get_artikel': get_artikel,
    }
    return render(request, template_name, context)
@login_required
@user_passes_test(is_operator)
def artikel_detail(request, id):
    template_name = 'back/artikel_detail.html'
    artikel = Artikel.objects.get(id=id)
    context = {
        'title' : 'DETAIL ARTIKEL',
        'artikel' : artikel,
    }
    return render(request, template_name, context)
def user_detail(request, id):
    template_name = 'back/user_detail.html'
    user = User.objects.get(id=id)
    context = {
        'title' : 'DETAIL USER',
        'user_detail' : user_detail,
    }
    return render(request, template_name, context)
@login_required
@user_passes_test(is_operator)
def artikel_delete (request, id):
    Artikel.objects.get(id=id).delete()
    return redirect(artikel_list)