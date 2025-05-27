from django.contrib import admin
from .models import  Player, Match, Coach, Team, MatchVote, HeadToHeadRecord

# admin.site.register(Tournament)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Match)
admin.site.register(Coach)
admin.site.register(MatchVote)
admin.site.register(HeadToHeadRecord)
