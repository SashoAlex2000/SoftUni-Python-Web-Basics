from django.contrib import admin

from notes_app_third.web.models import Profile, Note


# Register your models here.

@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Note)
class ProfileModelAdmin(admin.ModelAdmin):
    pass
