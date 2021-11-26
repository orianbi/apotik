from django.contrib import admin

# Register your models here.
from .models import Custemer, Obat, Order, Profile

# class CustemerAdmin(admin.ModelAdmin):
#     model = Custemer

# class ObatAdmin(admin.ModelAdmin):
#     model = Obat
    
# admin.site.register(Obat, ObatAdmin)

admin.site.register(Custemer)
admin.site.register(Obat)
admin.site.register(Order)
admin.site.register(Profile)

    