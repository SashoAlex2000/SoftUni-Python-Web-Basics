from django.contrib import admin

from models_django.web.models import Employee, Department, Project


# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'review')
    list_filter = ('first_name',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass
