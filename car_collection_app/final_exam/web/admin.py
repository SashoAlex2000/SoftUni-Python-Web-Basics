from django.contrib import admin

from final_exam.web.models import Profile, Car


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class Caradmin(admin.ModelAdmin):
    pass

