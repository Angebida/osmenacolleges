from django.contrib import admin
from .models import Department, Program, Faculty, News, Event, Application

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head_of_department', 'established_date')
    search_fields = ('name', 'head_of_department')
    list_filter = ('established_date',)

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'degree_type', 'duration_years', 'is_active')
    list_filter = ('department', 'degree_type', 'is_active')
    search_fields = ('name', 'department__name')

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'department', 'rank', 'is_active')
    list_filter = ('department', 'rank', 'is_active')
    search_fields = ('last_name', 'first_name', 'department__name')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date', 'is_featured')
    list_filter = ('publish_date', 'is_featured')
    search_fields = ('title', 'author')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'location', 'is_active')
    list_filter = ('start_date', 'is_active')
    search_fields = ('title', 'location')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'program', 'application_date', 'status')
    list_filter = ('status', 'start_term', 'program')
    search_fields = ('first_name', 'last_name', 'email')