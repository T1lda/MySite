from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted', 'author')
    list_filter = ('posted',)
    search_fields = ('title', 'short_content')
    date_hierarchy = 'posted'