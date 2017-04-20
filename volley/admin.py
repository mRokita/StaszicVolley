from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from volley.models import Post, Team, Player, Match


class PostAdmin(ModelAdmin):
    pass

class PlayerInline(admin.StackedInline):
    model = Player
    extra = 0

class TeamAdmin(ModelAdmin):
    inlines = [PlayerInline]
    list_display = ['name', 'email', 'rank']
    readonly_fields = ['rank']

    def rank(self, obj):
        points = 0
        for m in Match.objects.filter(team_a=obj):
            points += m.score_a - m.score_b
        for m in Match.objects.filter(team_b=obj):
            points += m.score_b - m.score_a
        return points


class MatchAdmin(ModelAdmin):
    list_display = ['team_a', 'team_b', 'score_a', 'score_b']


admin.site.register(Post, PostAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Match, MatchAdmin)