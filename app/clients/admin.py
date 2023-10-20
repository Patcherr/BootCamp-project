from django.contrib import admin
from clients.models import ClientModel
# Register your models here.

@admin.register(ClientModel)
class ClientAdmin(admin.ModelAdmin):
    pass