from django.contrib import admin
from .models import Driver

class DriverAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "latitude", "longitude", "is_available")
    list_filter = ("is_available",)
    search_fields = ("name",)