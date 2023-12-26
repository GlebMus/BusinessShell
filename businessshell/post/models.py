from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок",
        blank=False,
        null=False,
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='URl',
    )
    author = models.ForeignKey(
        verbose_name="автор",
        to=User,
        related_name="author_posts",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    body = models.TextField(
        verbose_name="Контент",
        blank=False,
        null=False,
    )
    created = models.DateTimeField(
        verbose_name="создан",
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name="обновлён",
        auto_now=True,
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    post = models.ForeignKey(
        verbose_name="Пост",
        to=Post,
        related_name="comment",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    author = models.ForeignKey(
        verbose_name="автор",
        to=User,
        related_name="author_comments",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    body = models.TextField(
        verbose_name="комментарий",
        blank=False,
        null=False,
    )
    created = models.DateTimeField(
        verbose_name="создан",
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name="обновлён",
        auto_now=True,
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"