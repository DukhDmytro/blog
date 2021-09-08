"""
Views related to posts, categories and topics
"""
from django.db.models import Prefetch
from rest_framework import viewsets

from .models import Post, Category, Topic
from .serializers import PostSerializer, CategorySerializer, TopicSerializer
from .permissions import IsAuthorOrReadOnly, IsAdminOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author').prefetch_related(
        Prefetch(
            'topics', queryset=Topic.objects.select_related('category').all()
        )
    ).all()
    serializer_class = PostSerializer

    def get_permissions(self) -> list:
        return super().get_permissions() + [IsAuthorOrReadOnly(), ]

    def perform_create(self, serializer: PostSerializer) -> None:
        serializer.save(author=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminOrReadOnly, ]
    lookup_field = 'slug'


class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.select_related('category').all()
    permission_classes = [IsAdminOrReadOnly, ]
    lookup_field = 'slug'
