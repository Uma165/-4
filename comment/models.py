from django.db import models
from django.contrib.auth.models import User
from cruise_list.models import Cruise


class Comment(models.Model):
    cruise = models.ForeignKey(Cruise, on_delete=models.CASCADE,
        related_name='comments', verbose_name='Круиз')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
        related_name='cruise_comments', verbose_name='Пользователь')

    text = models.TextField(blank=False, verbose_name="Текст комментария")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправления")

    def __str__(self):
        return self.text[:32] + '...'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-date_created',)
