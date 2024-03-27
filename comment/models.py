from django.db import models


class Comment(models.Model):
    text = models.TextField(blank=False, verbose_name="Текст комментария")
    date_of_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправления")

    def __str__(self):
        return self.text[:32] + '...'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-date_of_create',)
