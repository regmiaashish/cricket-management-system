from django.contrib import admin
from .models import Team, Player, Match, Coach

# admin.site.register(Tournament)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Match)
admin.site.register(Coach)
