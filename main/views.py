from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, redirect, HttpResponse
from .models import Custemer, Obat,  Order, Profile
from .forms import CustemerForm, ObatForm, OrderForm, UserForm, UserRoleForm
# Create your views here.

def home(request):
    judul ="Halaman Dashboard"
    konteks = {
        'judul':judul,
    }
    return render(request, 'home/home.html', konteks)

def obat(request):
    judul ="Halaman Obat"
    list_obat = Obat.objects.all()
    
    konteks = {
        'judul':judul,
        'list_obat':list_obat,
    }
    
    return render(request, 'obat/obat.html', konteks)

def addObat(request):
    judul = "Halaman Tambah Obat"
    
    if request.method == 'POST':
        form = ObatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('obat')
        else:
            return redirect('tambah_obat')
        
    else:
        form = ObatForm()
        
    konteks = {
        'judul':judul,
        'form':form,
    }
    
    return render(request, 'obat/tambah_obat.html', konteks)

def updateObat(request, pk):
    judul = "Halaman Edit Obat"
    
    obats = Obat.objects.get(id=pk)
    form = ObatForm(instance=obats)
    if request.method == 'POST':
        form = ObatForm(request.POST, instance=obats)
        if form.is_valid():
            form.save()
            return redirect('obat')
        
    konteks = {
        'judul':judul,
        'form':form,
    }
    return render(request, 'obat/edit_obat.html', konteks )

def deletObat(request, pk):
    delObat = Obat.objects.get(id=pk)
    delObat.delete()
    return redirect('obat')

def custemer(request):
    judul = "List Pelanggan"
    list_custemer = Custemer.objects.all()
    
    konteks = {
        'judul': judul,
        'custemer':list_custemer,
    }
    
    return render(request, 'pelanggan/pelanggan.html', konteks)

def addCustemer(request):
    judul ="Halaman Tambah Pelanggan"    
    if request.method == 'POST':
        form = CustemerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pelanggan')
        else:
            return redirect('tambah_pelanggan')
    else:
        form = CustemerForm()

    konteks = {
        'judul':judul,
        'form':form,
    }

    return render(request, 'pelanggan/tambah_pelanggan.html', konteks)
def updateCustemer(request, pk):
    judul = "Halaman Edit Pelanggan"
    
    custemers = Custemer.objects.get(id=pk)
    form = CustemerForm(instance=custemers)
    if request.method == 'POST':
        form = CustemerForm(request.POST, instance=custemers)
        if form.is_valid():
            form.save()
            return redirect('pelanggan')
        else:
            return redirect('edit_pelanggan')
    
    konteks = {
        'judul':judul,
        'form':form,
    }
    return render(request, 'pelanggan/edit_pelanggan.html', konteks)        

def deletCustemer(request,pk):
    delCustemer = Custemer.objects.get(id=pk)
    delCustemer.delete()
    return redirect('pelanggan')

def order(request):
    judul = "List Transaksi Pelanggan"
    
    list_order = Order.objects.order_by('-id')
    
    konteks = {
        'order':list_order,
    }
    
    return render(request,'transaksi/order.html', konteks)
def addOrder(request):
    judul = "Halaman Transaksi"
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaksi')
        else:
            return redirect('tambah_transaksi')
    else:
        form = OrderForm()
        
    konteks = {
        'judul':judul,
        'form':form,
    }
    
    return render(request, 'transaksi/tambah_order.html', konteks)
        
def user(request):
    judul = "Halaman User"
    users = User.objects.all()
    
    konteks = {
        'judul':judul,
        'users':users,
    }
    return render(request, 'user/user.html', konteks)


def addUser(request):
    judul = "Tambah User"
    if request.method == 'POST':
        form = UserForm(request.POST)
        role = UserRoleForm(request.POST)
        if form.is_valid() and role.is_valid():
            user = form.save()
            user.save()
            prof = role.save(commit=False)
            prof.user = user
            prof.save()
            return redirect('user')
    else:
        form = UserForm()
        role = UserRoleForm()
        
    konteks = {
        'judul':judul,
        'form':form,
        'role':role,
        }  
        
    return render(request, 'user/tambah_user.html', konteks)