from django.contrib import admin
from .models import Profile, Experience, Education, Project, Blog

# Register your models here
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')  # Fields to display in the admin list view
    search_fields = ('name', 'bio')  # Fields to search in the admin panel

# Register the Experience model in the admin panel
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date')  # Fields to display in the list view
    list_filter = ('company', 'start_date')  # Add filters for these fields
    search_fields = ('title', 'company', 'description')  # Add search functionality for these fields
    date_hierarchy = 'start_date'  # Add a date hierarchy for the start_date field

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'start_date', 'end_date', 'location')
    search_fields = ('institution', 'degree', 'location')
    list_filter = ('start_date', 'end_date')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'image', 'pdf_file', 'description')
    list_filter = ('type',)
    search_fields = ('title', 'description')

from django.contrib import admin
from .models import Blog, Comment, Reply

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published')
    search_fields = ('title', 'content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'name', 'date_posted')
    search_fields = ('name', 'content')

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('comment', 'name', 'date_posted')
    search_fields = ('name', 'content')
