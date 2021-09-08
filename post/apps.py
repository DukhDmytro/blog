"""
Post application configs
"""
from django.apps import AppConfig


class PostConfig(AppConfig):
    """
    Class containing Post app configs
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post'
