from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
import requests
from django.http import HttpResponse




from blog.models import Artikel, Berita


def index(request):
    url_berita= 'https://newsapi.org/v2/top-headlines?country=id&apiKey=9912598531fd4d709d708de5621a102b'
    kategori_berita = requests.get(url_berita)
    data_kategori_berita = kategori_berita.json()
    api_kategori_berita = data_kategori_berita['articles']


    

    template_name = 'front/index.html'
    artikel = Artikel.objects.all()
    search = request.GET.get('search')
    if request.GET.get('search'):
        url_berita= f'https://newsapi.org/v2/top-headlines?country=id&apiKey=9912598531fd4d709d708de5621a102b&q={search}'
        kategori_berita = requests.get(url_berita)
        data_kategori_berita = kategori_berita.json()
        api_kategori_berita = data_kategori_berita['articles']
        artikel = Artikel.objects.filter(judul__icontains=search)
    context = {
        
        'title ' : 'halaman awal',
        'artikel' :artikel,
        'api_kategori_berita' : api_kategori_berita
    }
    return render(request, template_name, context)
def detail_artikel(request, id):
    template_name = 'front/detail_artikel.html'
    artikel = Artikel.objects.get(id=id)
    context = {
        'title' : 'detail',
        'artikel': artikel
    }
    return render(request, template_name, context)
def about(request):
    template_name = 'front/about.html'
    context = {
        'title ' : 'tentang saya',
    }
    return render(request, template_name, context)
def login(request):
    template_name = 'account/login.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
                #data ada
            print('username benar')
            auth_login(request,user)
        else:
                #data tidak ada
            print('username salah')
    context = {
        'title ' : 'halaman login',
        'login' :login,
    }
    return render(request, template_name, context)
def logout_view(request):
    logout(request)
    return redirect('index')
