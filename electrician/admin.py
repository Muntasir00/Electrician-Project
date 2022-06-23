from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Electrician)
class ElectricianAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'rate', 'available']
    list_filter = ['available']
    list_editable = ['rate', 'available']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
    list_filter = ['email']
    # list_editable = ['name', 'email','message']
    
class OrderItemInline(admin.TabularInline):
     model = OrderItem
     raw_id_fields = ['electrician']
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email','electrician_id',
                    'address', 'postal_code', 'city', 'paid','created']
    list_filter = ['paid', 'created']
    inlines = [OrderItemInline]
