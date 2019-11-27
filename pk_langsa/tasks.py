from celery import task
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

from .models import Karyawan, Persekot


@task
def karyawan_created(karyawan_id):
    karyawan = Karyawan.objects.get(id=karyawan_id)
    subject = 'Karyawan dengan NPK nomor. {}'.format(karyawan.npk)
    message = 'Kepada {}, \n\nNPK anda telah dibuat. \
        NPK anda adalah {}.'.format(karyawan.nama,
                                    karyawan.npk)
    mail_sent = send_mail(subject,
                          message,
                          settings.EMAIL_HOST_USER,
                          [karyawan.email])
    return mail_sent


@task
def karyawan_jatuh_tempo(karyawan_id):
    karyawan = Karyawan.objects.get(id=karyawan_id)
    subject = 'Jatuh tempo Persekot untuk karyawan dengan NPK nomor {}'.format(
        karyawan.npk)
    message = 'Kepada {}, \n\nPersekot anda akan jatuh tempo dalam 3 hari. \
        NPK anda adalah {}.'.format(karyawan.nama,
                                    karyawan.npk)
    mail_sent = send_mail(subject,
                          message,
                          settings.EMAIL_HOST_USER,
                          [karyawan.email])
    return mail_sent
