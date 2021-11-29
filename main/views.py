from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse, reverse
from .models import Custemer, Obat,  Order, Profile
from .forms import CustemerForm, ObatForm, OrderForm, UserForm, UserRoleForm
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

def user_login(request):
    judul ="Halaman Login!"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username atau Password tidak benar!!!')
             
    konteks = {
        'judul':judul,
    }
    
    return render(request, 'auth/login.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def user_logout(request):
    logout(request)
    messages.success(request, "Logout Berhasil!!!")
    return HttpResponseRedirect(reverse('login'))

@login_required(login_url=settings.LOGIN_URL)
def home(request):
    judul ="Halaman Dashboard"
    konteks = {
        'judul':judul,
    }
    return render(request, 'home/home.html', konteks)
@login_required(login_url=settings.LOGIN_URL)
def obat(request):
    judul ="Halaman Obat"
    list_obat = Obat.objects.all()
    
    konteks = {
        'judul':judul,
        'list_obat':list_obat,
    }
    
    return render(request, 'obat/obat.html', konteks)
@login_required(login_url=settings.LOGIN_URL)
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

@login_required(login_url=settings.LOGIN_URL)
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

@login_required(login_url=settings.LOGIN_URL)
def deletObat(request, pk):
    delObat = Obat.objects.get(id=pk)
    delObat.delete()
    return redirect('obat')

@login_required(login_url=settings.LOGIN_URL)
def custemer(request):
    judul = "List Pelanggan"
    list_custemer = Custemer.objects.all()
    
    konteks = {
        'judul': judul,
        'custemer':list_custemer,
    }
    
    return render(request, 'pelanggan/pelanggan.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
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

@login_required(login_url=settings.LOGIN_URL)
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

@login_required(login_url=settings.LOGIN_URL)
def deletCustemer(request,pk):
    delCustemer = Custemer.objects.get(id=pk)
    delCustemer.delete()
    return redirect('pelanggan')

@login_required(login_url=settings.LOGIN_URL)
def order(request):
    judul = "List Transaksi Pelanggan"
    
    list_order = Order.objects.order_by('-id')
    
    konteks = {
        'order':list_order,
    }
    
    return render(request,'transaksi/order.html', konteks)
@login_required(login_url=settings.LOGIN_URL)
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


@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda user: user.profile.role == 'Admin')      
def user(request):
    judul = "Halaman User"
    users = User.objects.all()
    
    konteks = {
        'judul':judul,
        'users':users,
    }
    return render(request, 'user/user.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda user: user.profile.role == 'Admin')
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