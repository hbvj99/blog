from django.contrib import admin
from blog.models import Blog, Author


class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ('author', 'title', 'slug', 'description', 'image', 'created_at', 'updated_at')
    list_filter = ('author', 'created_at', 'updated_at')
    search_fields = ('title', 'slug', 'description')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('name', 'email')
    search_fields = ('name', 'email')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.site_header = 'Personal Blog'
