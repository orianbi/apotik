
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    
    ROLE_CHOICES = (
        ('Admin','Admin'),       
        ('User','User'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    def __str__(self):
        return self.user.username
    
    
class Custemer(models.Model):
    kode_custemer = models.CharField(max_length=50, blank=True, null=True)
    name_custemer = models.CharField(max_length=50, blank=True, null=True)
    email_custemer = models.EmailField(max_length=254, blank=True, null=True)
    telpon_custemer = models.CharField(max_length=50, blank=True, null=True)
    alamat_custemer = models.TextField()
    
    def __str__(self):
        return self.name_custemer
class Obat(models.Model):
    kode_obat = models.CharField(max_length=50)
    name_obat = models.CharField(max_length=50)
    price_obat = models.IntegerField(blank=True, null=True)
    stok_obat = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=False, null=True)
    
    def __str__(self):
        return self.name_obat
    
class Order(models.Model):
    obat_id = models.ForeignKey(Obat, null=True, on_delete=models.SET_NULL)
    custemer_id = models.ForeignKey(Custemer, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    qty_order = models.IntegerField(blank=True, null=True)
    qty_price = models.IntegerField(blank=True,null=True)
    discon = models.IntegerField(blank=True, null=True)
    price_after_disc = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.obat_id.name_obat
    
   