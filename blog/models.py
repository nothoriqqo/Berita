from django.db import models 
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Kategori(models.Model):
    nama = models.CharField(max_length=20)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "Kategori"

class Artikel(models.Model):
    nama = models.CharField(max_length=100, blank=True, null=True)
    judul = models.CharField(max_length=100)
    body = RichTextUploadingField(blank=True, null=True,
                                    config_name='special',
                                    external_plugin_resources=[(
                                    'youtube',
                                    'static/ckeditor_plugins/youtube/youtube',
                                    'plugin.js',
                                    )],)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.nama, self.judul)

    class Meta:
        verbose_name_plural = "Artikel"
class Berita(models.Model):
    title = models.TextField()
    description = models.TextField()
    url = models.TextField()
    url_image = models.TextField()
    author = models.TextField()
    publishedAt = models.TextField()
class Users(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100)
    fisrt_name = models.TextField()
    last_name = models.TextField()
    
    def __str__(self):
        return "{} - {}".format(self.name, self.email)

    class Meta:
        verbose_name_plural = "Users"

    