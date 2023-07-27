from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'blog_post', 'content', 'created_at', 'updated_at')
    list_filter = ('blog_post', 'author', 'created_at', 'updated_at')
    search_fields = ('content', 'author__username', 'blog_post__title')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Comment, CommentAdmin)
