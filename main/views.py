from django.http import request
from django.shortcuts import render, redirect, HttpResponse
from .models import Custemer, Obat,  Order
from .forms import CustemerForm, ObatForm
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
    judul = "Halaman Pelanggan"
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
    judul = "Halaman Transaksi Pelanggan"
    
    list_order = Order.objects.order_by('-id')
    
    konteks = {
        'order':list_order,
    }
    
    return render(request,'transaksi/order.html', konteks)
