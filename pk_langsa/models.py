from django.db import models
from datetime import timedelta

# Create your models here.

UNIT_KERJA = [
    (1, 'Kepesertaan'),
    (2, 'Pelayanan'),
    (3, 'Keuangan'),
    (4, 'Umum & SDM'),
]


class Karyawan(models.Model):
    nama = models.CharField(max_length=50)
    npk = models.CharField(max_length=9)
    unit_kerja = models.IntegerField(choices=UNIT_KERJA)
    no_hp = models.CharField(max_length=13)
    email = models.EmailField()
    

    def __str__(self):
        return '%s - %s' % (self.nama, self.npk)


class Persekot(models.Model):
    karyawan = models.ForeignKey(Karyawan, on_delete=models.CASCADE)
    keterangan = models.TextField()
    nominal = models.DecimalField(max_digits=13, decimal_places=2)
    tgl_pk = models.DateField()

    def jatuh_tempo(self):
        return self.tgl_pk + timedelta(days=14)


class PetanggungJawabanPersekot(models.Model):
    persekot = models.ForeignKey(Persekot, on_delete=models.CASCADE)
    tgl_selesai_pk = models.DateField()
