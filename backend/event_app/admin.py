from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "dateDebut", "dateFin", "participation")
    search_fields = ("name", "description")
    list_filter = ("dateDebut","dateFin")