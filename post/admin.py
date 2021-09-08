"""
Register models for admin panel here.
"""
from django.contrib import admin

from post.models import Category, Topic, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Class containing display options for Category class
    in admin panel.
    """
    list_display = ('title', 'slug', 'description')


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    """
    Class containing display options for Topic class
    in admin panel.
    """
    list_display = ('title', 'slug', 'description')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Class containing display options for Post class
    in admin panel.
    """
    list_display = ('title', 'body')
