from django.contrib import admin
from .models import User, Pokemon, Competence

# Enregistrer les modèles avec l'interface d'administration
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'hp')
    search_fields = ('name', 'type')

@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'damage', 'accuracy')
    search_fields = ('name', 'type')
