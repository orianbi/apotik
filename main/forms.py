from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets

from django.utils.translation import gettext_lazy as _

from .models import Custemer, Obat, Order


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
            'price_obat': widgets.NumberInput(attrs={'class':'form-control','autocomplete':'off'}),
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
            'qty_order': widgets.NumberInput(attrs={'class':'form-control','autocomplete':'off'}),
        }