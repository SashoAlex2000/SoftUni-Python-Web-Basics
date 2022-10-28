from django.contrib import admin

from games_play_app.web.models import Profile, Game


# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Game)
class ProfileAdmin(admin.ModelAdmin):
    pass
