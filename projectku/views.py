from django.shortcuts import render
from blog.models import Artikel

def index(request):
    template_name = 'front/index.html'
    artikel = Artikel.objects.all()
    context = {
        'title ' : 'halaman awal',
        'artikel' :artikel,
    }
    return render(request, template_name, context)
def about(request):
    template_name = 'front/about.html'
    context = {
        'title ' : 'tentang saya',
    }
    return render(request, template_name, context)
def login(request):
    template_name = 'front/login.html'
    context = {
        'title ' : 'halaman login',
        'login' :login,
    }
    return render(request, template_name, context)
def register(request):
    template_name = 'front/register.html'
    context = {
        'title ' : 'halaman register',
        'register' :register,
    }
    return render(request, template_name, context)