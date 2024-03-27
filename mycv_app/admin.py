from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.


admin.site.site_header = "Admin myCv"
admin.site.site_title = "myCv"
admin.site.index_title = "Admin myCv"

class BeritaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'judul', 'deskripsi', 'created', 'image_tag')
    list_filter = ('id', 'judul', 'deskripsi', 'created')
    search_fields = ('id', 'judul', 'deskripsi', 'created')

admin.site.register(Berita, BeritaAdmin)


class TestimoniAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'nama', 'email', 'deskripsi')
    list_filter = ('id', 'nama', 'email', 'deskripsi')
    search_fields = ('id', 'nama', 'email', 'deskripsi')

admin.site.register(Testimoni, TestimoniAdmin)