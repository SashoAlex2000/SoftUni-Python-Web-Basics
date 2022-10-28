from django.contrib import admin

from library_past_exam.web.models import Profile, Book


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class ProfileAdmin(admin.ModelAdmin):
    pass
