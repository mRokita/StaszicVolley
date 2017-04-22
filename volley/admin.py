from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from volley.models import Post, Team, Player, Match, Tournament


class PostAdmin(ModelAdmin):
    pass

class PlayerInline(admin.StackedInline):
    model = Player
    extra = 0


class TournamentAdmin(ModelAdmin):
    pass


class TeamAdmin(ModelAdmin):
    inlines = [PlayerInline]
    list_display = ['name', 'email', 'rank']
    readonly_fields = ['rank']

    def rank(self, obj):
        return obj.get_rank()


class MatchAdmin(ModelAdmin):
    list_display = ['team_a', 'team_b', 'score_a', 'score_b']


admin.site.register(Post, PostAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Tournament, TournamentAdmin)