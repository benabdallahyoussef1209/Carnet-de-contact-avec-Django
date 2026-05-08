from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Configuration du panneau d'administration pour les contacts."""
    list_display = ['prenom', 'nom', 'email', 'telephone', 'date_creation']
    search_fields = ['prenom', 'nom', 'email']
    list_filter = ['date_creation']
    ordering = ['nom', 'prenom']
