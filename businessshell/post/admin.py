from django.contrib import admin
from .models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    fields = ['author', 'body', 'created', 'updated']
    readonly_fields = ['created', 'updated']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'updated')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created', 'updated')
    readonly_fields = ['created', 'updated']
