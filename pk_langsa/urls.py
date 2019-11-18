from django.urls import path

from . import views

app_name = 'pk_langsa'
urlpatterns = [
    path('karyawan/<int:pk>/delete', views.karyawan_delete, name='karyawan_delete'),
    path('karyawan/<int:pk>/edit', views.karyawan_edit, name='karyawan_edit'),
    path('karyawan/<int:pk>/', views.karyawan_detail, name='karyawan_detail'),
    path('karyawan/new/', views.karyawan_new, name='karyawan_new'),
    path('karyawan/', views.karyawan_list, name='karyawan_list'),
    path('pk_list', views.pk_list, name='pk_list'),
    path('', views.index, name='pk_langsa'),


]
