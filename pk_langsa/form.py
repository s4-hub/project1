from django import forms
from .models import Karyawan, Persekot, PetanggungJawabanPersekot


class KaryawanForm(forms.ModelForm):
    class Meta:
        model = Karyawan
        fields = ['npk', 'nama',
                  'unit_kerja',
                  'no_hp',
                  'email'
                  ]
        widgets = {
            'nama': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Masukkan nama anda', }),
            'npk': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Masukkan NPK anda', }),
            'unit_kerja': forms.Select(
                attrs={'class': 'form-control',
                       'placeholder': 'Masukkan Unit Kerja anda', }),
            'no_hp': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Masukkan No WA Anda', }),
            'email': forms.TextInput(
                attrs={'class': 'form-control',
                       'type': 'email',
                       'placeholder': 'Masukkan email anda', }),
        }
