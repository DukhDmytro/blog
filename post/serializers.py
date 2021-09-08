"""
Serializers for post app models
"""
from rest_framework import serializers

from .models import Post, Category, Topic


class CategorySerializer(serializers.ModelSerializer):
    """
    Category model serializer
    """
    class Meta:
        model = Category
        fields = ['slug', 'title', 'description']


class TopicSerializer(serializers.ModelSerializer):
    """
    Topic model serializer
    """

    category = serializers.SlugRelatedField(slug_field='slug',
                                            queryset=Category.objects.all())

    class Meta:
        model = Topic
        fields = ['slug', 'title', 'description', 'category']

    def to_representation(self, instance: Topic) -> dict:
        """
        Method used to display category field as nested serializer.
        """
        result = super().to_representation(instance)
        result['category'] = CategorySerializer(instance.category).data
        return result


class PostSerializer(serializers.ModelSerializer):
    """
    Post model serializer
    """
    author = serializers.ReadOnlyField(source='author.username')
    queryset = Topic.objects.select_related('category').all()
    topics = serializers.SlugRelatedField(slug_field='slug',
                                          queryset=queryset,
                                          many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'author', 'topics']

    def to_representation(self, instance: Post) -> dict:
        """
        Method used to display topics field as nested serializer.
        """
        result = super().to_representation(instance)
        result['topics'] = TopicSerializer(instance.topics, many=True).data
        return result

    def validate_topics(self, value: list[Topic]) -> list[Topic]:
        """
        :param value: list of Topic instances
        :return: list of Topic instances
        :raise: ValidationError in case when user try
            to create post without topic.
        """
        if not value:
            raise serializers.ValidationError(
                'Post without topics is not allowed'
            )
        return value
