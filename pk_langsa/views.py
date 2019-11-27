from django.shortcuts import render, redirect, get_object_or_404
from . models import Karyawan, Persekot
from .form import KaryawanForm
from .tasks import karyawan_created, karyawan_jatuh_tempo

# Create your views here.


def index(request):

    datas = Karyawan.objects.all()
    return render(request, 'pk_langsa/index.html', {'datas': datas})


def pk_list(request):
    datas = Persekot.objects.all()
    return render(request, 'pk_langsa/pk_list.html', {'datas': datas})


def karyawan_new(request):
    if request.method == "POST":
        form = KaryawanForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            karyawan_created.delay(post.id)
            karyawan_jatuh_tempo.apply_async((post.id,),
                                             countdown=60)
            return redirect('pk_langsa:karyawan_list')
    else:
        form = KaryawanForm()
    return render(request, 'pk_langsa/karyawan_edit.html', {'form': form})


def karyawan_list(request):
    datas = Karyawan.objects.all()
    return render(request, 'pk_langsa/karyawan_list.html', {'datas': datas})


def karyawan_edit(request, pk):
    data_master = get_object_or_404(Karyawan, pk=pk)
    if request.method == 'POST':
        form = KaryawanForm(request.POST, instance=data_master)
        if form.is_valid():
            data_master = form.save(commit=False)
            data_master.save()
            return redirect('pk_langsa:karyawan_detail', pk=data_master.pk)
    else:
        form = KaryawanForm(instance=data_master)
    return render(request, 'pk_langsa/karyawan_edit.html', {'form': form})


def karyawan_detail(request, pk):
    datas = get_object_or_404(Karyawan, pk=pk)
    return render(request, 'pk_langsa/karyawan_detail.html', {'datas': datas})


def karyawan_delete(request, pk):

    post = get_object_or_404(Karyawan, pk=pk)
    post.delete()
    return redirect('pk_langsa:karyawan_list')
