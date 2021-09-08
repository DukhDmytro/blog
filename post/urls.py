"""
Post app routing
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'post'

router = DefaultRouter()
router.register('categories', views.CategoryViewSet)
router.register('topics', views.TopicViewSet)
router.register('posts', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
