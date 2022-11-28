from django.contrib import admin
from sgCampeonato.models import Player
from sgCampeonato.models import Team

class PlayerAdmin(admin.ModelAdmin):
    list_display=("name", "number", "goals", "rc")

# Register your models here.

admin.site.register(Player, PlayerAdmin)
admin.site.register(Team)