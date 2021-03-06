from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("login/", views.user_login, name="login"),
    path('logout/', views.user_logout, name='logout'),
    path('obat/', views.obat, name='obat'),
    path('tambah_obat/', views.addObat, name='tambah_obat'),
    path('edit_obat/<str:pk>/', views.updateObat, name='edit_obat' ),
    path('hapus_obat/<str:pk>/', views.deletObat, name='hapus_obat'),
    path('pelanggan/', views.custemer, name='pelanggan'),
    path('tambah_pelanggan/', views.addCustemer, name='tambah_pelanggan'),
    path('edit_pelanggan/<str:pk>/', views.updateCustemer, name='edit_pelanggan'),
    path('hapus_pelanggan/<str:pk>/', views.deletCustemer, name='hapus_pelanggan'),
    path('transaksi/', views.order, name='transaksi'),
    path('tambah_transaksi/', views.addOrder, name='tambah_transaksi'),
    path('user/', views.user, name="user"),
    path('tambah_user/', views.addUser, name="tambah_user"),
    
]

