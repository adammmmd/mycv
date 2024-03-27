from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class Berita (models.Model):
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField()
    kategori = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='images', blank=True, null=True)

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.cover.url))
    image_tag.short_description = 'Cover'

class Testimoni (models.Model):
    nama = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    deskripsi = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
