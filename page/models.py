from django.db import models


class Page(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название круиза')
    description = models.TextField(verbose_name='Описание круиза')
    image = models.ImageField(upload_to='%Y/%m/%d', blank=True, null=True)

    class Meta:
        verbose_name = 'Круиз'
        verbose_name_plural = 'Круиз'

