from django.db import models


class Сruise(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    time = models.CharField(max_length=60, verbose_name='Время круиза')
    сities = models.CharField(max_length=128, verbose_name='Название городов')
    discription =models.TextField(verbose_name='Описание')
    price = models.CharField(max_length=100, verbose_name='Стоимость')
    publish_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    edit_date = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Дата редактирования')
    image = models.ImageField(upload_to='%Y/%m/%d', blank=True, null=True)
    view = models.CharField(max_length=128, verbose_name='Просмотры')

    class Meta:
        verbose_name = 'Маршруты и корабли'
        verbose_name_plural = 'Маршруты и корабли'
        ordering = ('-publish_date', '-edit_date')