from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from volley.models import Post, Team, Player


class PostAdmin(ModelAdmin):
    pass

class PlayerInline(admin.StackedInline):
    model = Player
    extra = 0

class TeamAdmin(ModelAdmin):
    inlines = [PlayerInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Team, TeamAdmin)