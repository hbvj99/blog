from django.contrib import admin
from blog.models import Post


class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ('title', 'slug', 'description', 'image', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'slug', 'description')


admin.site.register(Post, BlogAdmin)
admin.site.site_header = 'Blog | Dashboard'
