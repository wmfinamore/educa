from django.contrib import admin
from .models import (Subject,
                     Course,
                     Module)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class ModuleInLine(admin.StackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fields = (('owner', 'subject'), ('title', 'slug'), 'overview')
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInLine]


# use memcache admin index site
admin.site.index_template = 'memcache_status/admin_index.html'
