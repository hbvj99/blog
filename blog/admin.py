from django.contrib import admin
from blog.models import Post, Author


class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ('author', 'title', 'slug', 'description', 'image', 'created_at', 'updated_at')
    list_filter = ('author', 'created_at', 'updated_at')
    search_fields = ('title', 'slug', 'description')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    list_filter = ('name', 'created_at')
    search_fields = ('name', 'created_at')


admin.site.register(Post, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.site_header = 'Blog | Dashboard'
