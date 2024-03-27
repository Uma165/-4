from django.contrib.auth.models import User
from django.db import models


class Appeal(models.Model):
    TYPES = (
        ('Вечерний путь', 'Вечерний путь'),
        ('Моряк', 'Моряк'),
        ('Рай над морем', 'Рай над морем'),
        ('Воздушный корабль', 'Воздушный корабль'),
    )

    STATUS_CHOICE = (("a", "В обработке"),
                     ("b", "Выполнено"),
                     ("c", "Отклонено"))

    type = models.CharField(choices=TYPES, max_length=128, verbose_name='Круиз')
    сapacity = models.CharField(max_length=60, verbose_name='Количество человек')
    contact = models.CharField(max_length=128, verbose_name='Контактая информация')
    email = models.EmailField("Электронная почта", blank=False)
    status = models.CharField(max_length=100, verbose_name='Статус', choices=STATUS_CHOICE)
    uid = models.CharField(max_length=64, blank=False, null=False, db_index=True, unique=True)
    date = models.DateTimeField("Дата отправки", auto_now_add=True)

    def __iter__(self):
        for field in self._meta.fields:
            yield field.verbose_name, field.value_to_string(self)

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
        #ordering = ('-date', )


class Answer(models.Model):
    text = models.TextField(blank=False)
    file = models.FileField(upload_to='answer/%Y/%m/%d', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Профиль')
    send_date = models.DateTimeField('Дата отправки', auto_now_add=True)
    update_date = models.DateTimeField('Дата редактирования', auto_now=True)
    appeal = models.OneToOneField(Appeal, on_delete=models.CASCADE, related_name='answer', verbose_name='Заявка')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ('-send_date', '-update_date')
