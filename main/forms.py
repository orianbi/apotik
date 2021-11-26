from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from .models import Custemer, Obat, Order, Profile


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2',)
        
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','autocomplete':'off'}),
            'email':forms.EmailInput(attrs={'class':'form-control','autocomplete':'off'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control','autocomplete':'off'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control','autocomplete':'off'}),
           
        }
class UserRoleForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('role',)
        
        widgets = {
            'role':forms.Select(attrs={'class':'form-control',"autocomplete":"off"}),          
        }

        labels = {                     
            'role':'Level User',
         }
        
class CustemerForm(ModelForm):
    class Meta:
        model = Custemer
        fields = '__all__'
        
        widgets = {
            'kode_custemer':widgets.TextInput(attrs={'class':'form-control','autocomplete':'off'}),
            'name_custemer':widgets.TextInput(attrs={'class':'form-control','autocomplete':'off'}),
            'email_custemer':widgets.EmailInput(attrs={'class':'form-control','autocomplete':'off'}),
            'telpon_custemer':widgets.TextInput(attrs={'class':'form-control','autocomplete':'off'}),
            'alamat_custemer':widgets.Textarea(attrs={'class':'form-control','autocomplete':'off'}),
        }
        
        labels = {
            'kode_custemer': 'KODE CUSTEMER',
            'name_custemer': 'NAMA CUSTEMER',
            'email_custemer': 'EMAIL CUSTEMER',
            'telpon_custemer': 'TELPON CUSTEMER',
            'alamat_custemer': 'ALAMAT CUSTEMER',
        }
        
        
class ObatForm(ModelForm):
    
    class Meta:        
        model = Obat
        fields = '__all__'
    
        widgets = {
            'kode_obat': widgets.TextInput(attrs={'class':'form-control','autocomplete':'off'}),
            'name_obat': widgets.TextInput(attrs={'class':'form-control','autocomplete':'off'}),
            'price_obat': widgets.NumberInput(attrs={'class':'form-control','autocomplete':'off','id':'price_obat'}),
            'stok_obat': widgets.NumberInput(attrs={'class':'form-control','autocomplete':'off'}),
            'description': widgets.Textarea(attrs={'class':'form-control','autocomplete':'off'}),
            'date_created': widgets.DateTimeInput(attrs={'class':'form-control','autocomplete':'off'}),
        }
        
        labels = {
            'kode_obat':'KODE OBAT',
            'name_obat':'NAMA OBAT',
            'price_obat':'HARGA OBAT',
            'stok_obat':'STOK OBAT',
            'description':'DESKRIPSI OBAT',
            'date_created':'TANGGAL PEMBELIAN OBAT',
        }
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        
        widgets = {
            'obat_id': forms.Select(attrs={'class':'form-control','autocomplete':'off'}),
            'custemer_id': forms.Select(attrs={'class':'form-control','autocomplete':'off'}),
            'date_created': widgets.DateTimeInput(attrs={'class':'form-control','autocomplete':'off'}),
            'qty_order': widgets.NumberInput(attrs={'class':'form-control','autocomplete':'off','id':'qty_order'}),
            'qty_price': widgets.NumberInput(attrs={'class':'form-control','autocomplete':'off', 'id':'qty_price'}),
            'discon': widgets.NumberInput(attrs={'class':'form-control','autocomplete':'off'}),
            'price_after_disc': widgets.NumberInput(attrs={'class':'form-control','autocomplete':'off'}),
        }
        
        labels = {
            'obat_id':'NAMA OBAT',
            'custemer_id':'NAMA CUSTEMER',
            'qty_order':'JUMLAH BELI',
            'qty_price':'TOTAL HARGA',
            'discon':'DISKON',
            'price_after_disc':'TOTAL HARGA SETELAH DISKON',
        }