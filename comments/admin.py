from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at', 'blog_post', 'card')
    search_fields = ('content', 'user__username')
    list_filter = ('created_at', 'user', 'blog_post', 'card')
