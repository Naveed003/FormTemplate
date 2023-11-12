from django.contrib import admin
from main.models import contracts

@admin.register(contracts)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']