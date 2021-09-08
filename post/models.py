"""
Post app models
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CategoryAbstractModel(models.Model):
    """
    Class containing common fields and methods for
    Category and Topic models.
    """
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=15, unique=True)

    class Meta:
        ordering = ('title',)
        abstract = True

    def __str__(self) -> str:
        return str(self.title)


class Category(CategoryAbstractModel):
    """
    Class describing Category model.
    The Category is a general subject of the post.
    """
    class Meta(CategoryAbstractModel.Meta):
        verbose_name = _('Категорія')
        verbose_name_plural = _('Категорії')


class Topic(CategoryAbstractModel):
    """
    Class describing Topic model.
    The Topic is related to category. Topic is
    more specific subject for the post.
    """
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='topics'
    )

    class Meta(CategoryAbstractModel.Meta):
        verbose_name = _('Тема')
        verbose_name_plural = _('Теми')


class Post(models.Model):
    """
    Class describing Post model.
    The Post is related to some topics.
    """
    topics = models.ManyToManyField(Topic, related_name='posts')
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=5000)
    author = models.ForeignKey('auth.User', related_name='posts',
                               on_delete=models.PROTECT
                               )

    class Meta:
        verbose_name = _('Допис')
        verbose_name_plural = _('Дописи')
