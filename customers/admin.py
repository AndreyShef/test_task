from django.contrib import admin
from .models import UserContacts
# Register your models here.

class CustomerAdm(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone')

admin.site.register(UserContacts, CustomerAdm)
