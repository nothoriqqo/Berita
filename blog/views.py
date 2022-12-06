from multiprocessing import context
from pyexpat.errors import messages
from turtle import title
from django.shortcuts import render, redirect
from blog.models import Artikel, Kategori
from django.http import HttpResponse

def artikel_list(request):
    template_name = 'back/table_artikel.html'
    artikel_list = Artikel.objects.all()
    context = {
        'title ' : 'halaman awal artikel',
        'artikel':artikel_list
    }
    return render(request, template_name, context)
def users(request):
    template_name = 'back/table_users.html'
    context = {
        'title' : 'tabel users',
    }
    return render(request, template_name, context)

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

def artikel_detail(request, id):
    template_name = 'back/artikel_detail.html'
    artikel = Artikel.objects.get(id=id)
    context = {
        title : 'Lihat detail artikel'
        
    }

def artikel_delete (request, id):
    Artikel.objects.get(id=id).delete()
    if request.method == 'POST':
        messages.success(request, "Sukses Menghapus Artikel." )
        return redirect(artikel_list)