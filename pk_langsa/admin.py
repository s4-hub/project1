from django.contrib import admin
from . models import Karyawan, Persekot
from datetime import timedelta

# Register your models here.


@admin.register(Karyawan)
class KaryawanAdmin(admin.ModelAdmin):
    list_display = ('nama', 'npk', 'email')
    search_fields = ('nama', 'npk', 'email')
    ordering = ('npk', 'nama')


@admin.register(Persekot)
class PersekotAdmin(admin.ModelAdmin):
    list_display = ('karyawan', 'keterangan',
                    'nominal', 'tgl_pk', 'jatuh_tempo')
    search_fields = ('karyawan', 'tgl_pk')
    ordering = ('karyawan', 'tgl_pk')

    