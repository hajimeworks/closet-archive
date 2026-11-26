from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("__str__", "category", "brand", "price", "status")
    list_filter = ("category", "status")
    search_fields = ("name", "brand")
    