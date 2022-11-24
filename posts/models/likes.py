from django.contrib.auth import get_user_model
from django.db import models


class Like(models.Model):
    author = models.ForeignKey(verbose_name='Автор',
                               to=get_user_model(),
                               related_name='likes',
                               null=False,
                               blank=False,
                               on_delete=models.CASCADE)
    posts = models.ManyToManyField(verbose_name='Публикации с лайком',
                                   to='posts.Post',
                                    related_name='posts_likes')
    is_like = models.BooleanField(
        verbose_name='Лайк',
        default=False, null=False
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
