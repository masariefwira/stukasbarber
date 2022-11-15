from django.urls import path
from . import views
urlpatterns = [
  path('home',views.home, name='home'),
  path('pelayan', views.pelayan, name='pelayan'),
  path('add_pelayan', views.add_pelayan, name='add_pelayan'),
  path('layanan', views.layanan, name='layanan'),
  path('transaksi', views.transaksi, name='transaksi'),
  path('add_transaksi', views.add_transaksi, name='add_transaksi'),
  path('detail_layanan/<str:id>', views.detail_layanan, name='detail_layanan'),
  path('detail_layanan/<str:id>/update', views.update_detail_layanan, name='update_detail_layanan'),
  path('delete_layanan/<str:id>/delete', views.delete_detail_layanan, name='delete_detail_layanan'),
  path('add_detail_layanan', views.add_detail_layanan, name='add_detail_layanan'),
  path('add_layanan', views.add_layanan, name='add_layanan'),
  path('layanan/<str:id>/update', views.update_layanan, name='update_layanan'),
  path('layanan/<str:id>/delete', views.delete_layanan, name='delete_layanan'),
  path('pelayan/<str:id>/update', views.update_pelayan, name='update_pelayan'),
  path('pelayan/<str:id>/delete', views.delete_pelayan, name='delete_pelayan'),
  path('transaksi/<str:id>/update', views.update_transaksi, name='update_transaksi'),
  path('transaksi/<str:id>/delete', views.delete_transaksi, name='delete_transaksi'),
  path('notapdf/<str:id>/',views.notapdf,name='notapdf'), 
  path('laporan',views.laporan,name='laporan'),
  path('laporanpdf/<str:mulai>/<str:akhir>',views.laporanpdf,name='laporanpdf'),
  
]